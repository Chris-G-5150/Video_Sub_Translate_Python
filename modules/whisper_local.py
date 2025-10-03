import GPUtil
from faster_whisper import WhisperModel
from tqdm import tqdm
import warnings
import torch
from data_classes.speech_chunk import SpeechChunk
from module_parameters.whisper_local_params import WhisperLocalParams


class WhisperLocal:
    def __init__(
            self,
            params: WhisperLocalParams,
    ):
        self.media_manager = params.media_manager
        self.file_manager = params.file_manager
        self.chosen_model = params.chosen_model
        self.video_card_details = GPUtil.getGPUs()

    def clear_chosen_model(self):
        self.chosen_model = None

    def gpu_is_compatible(self) -> bool:
        gpu = self.video_card_details
        gpu_is_compatible = bool(gpu and gpu[0].memoryTotal >= 1500)
        print("GPU is compatible")
        return gpu_is_compatible

    def write_transcriptions_to_disk(self):
        file_manager = self.file_manager
        directories = file_manager.directories
        media_manager_params = self.media_manager

        for index, chunk in enumerate(self.media_manager.silence_removed_speech_chunks):
            transcription_dir = directories.transcription_source_language_dir
            file_path = file_manager.build_file_os_path(f"{transcription_dir}", f"{str(index)}-{media_manager_params.project_title}-{media_manager_params.source_language}.txt")
            file_manager.write_text_file_to_disk(chunk.transcription_source_language_text, file_path)

        return 'Complete'

    def run_speech_to_text(self):
        media_manager = self.media_manager
        device = "cuda" if self.gpu_is_compatible() else "cpu"
        compute_type = "float16" if device == "cuda" else "int8"

        # Load faster-whisper model
        model = WhisperModel(self.chosen_model, device=device, compute_type=compute_type)
        chunks = media_manager.silence_removed_speech_chunks

        for i, chunk in enumerate(tqdm(chunks, desc="Transcribing")):
            try:
                language = media_manager.source_language
                if language or language != 'en':
                    segments, info = model.transcribe(str(chunk.speech_chunk_path), language=language)
                else:
                    segments, info = model.transcribe(str(chunk.speech_chunk_path))

                text = " ".join([seg.text for seg in segments])
                chunk.transcribed_audio_text = text

            except RuntimeError as e:
                if "CUDA out of memory" in str(e):
                    warnings.warn(
                        f"CUDA OOM on chunk {i} ({chunk.speech_chunk_path}). "
                        f"Try smaller model or run on CPU."
                    )
                else:
                    warnings.warn(
                        f"RuntimeError transcribing chunk {i} ({chunk.speech_chunk_path}): {e}"
                    )
                chunk.transcribed_audio_text = "[ERROR: failed to transcribe]"
                torch.cuda.empty_cache()  # clear GPU memory just in case

            except Exception as e:
                warnings.warn(
                    f"Unexpected error on chunk {i} ({chunk.speech_chunk_path}): {e}"
                )
                chunk.transcribed_audio_text = "[ERROR: failed to transcribe]"

            finally:
                # Always set platform field, even on failure
                chunk.platform_transcribed_from = f"Faster-Whisper-{self.chosen_model}"

        return "Complete"


    @staticmethod
    def process_transcription_results(results_list, chunk: SpeechChunk):
        chunk_transcribed = []
        if len(results_list) > 1:
            for result in results_list:
                if result.text == "":
                    warnings.warn(
                        f"No transcription for {chunk.clip_srt_index}, will skip between {chunk.milisecond_start} and {chunk.milisecond_end} and continue")
                else:
                    chunk_transcribed.append(f"{chunk.clip_srt_index}: {result.text}")
        else:
            chunk_transcribed.append(results_list.text)

        return str(chunk_transcribed)



 # whisper_local = WhisperLocal()

