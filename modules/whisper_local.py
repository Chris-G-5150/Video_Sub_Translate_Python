import warnings
from typing import List

import GPUtil
import torch
from faster_whisper import WhisperModel
from tqdm import tqdm

from data_classes.global_config import GlobalConfig
from data_classes.speech_chunk import SpeechChunk


class WhisperLocal:
	def __init__(
		self,
		global_config: GlobalConfig,
		speech_chunks: List[SpeechChunk],
	):
		self.global_config = global_config
		self.project_title = global_config.project_title
		self.transcription_dir = global_config.app_directories.transcription_source_language_dir  # type: ignore
		self.media_data = global_config.media_data
		self.speech_chunks = speech_chunks
		self.chosen_whisper_model = global_config.whisper_local_chosen_model
		self.video_card_details = GPUtil.getGPUs()  # pyright: ignore[reportUnknownMemberType]

	def gpu_is_compatible(self) -> bool:
		gpu = self.video_card_details  # type: ignore
		gpu_is_compatible = bool(gpu and gpu[0].memoryTotal >= 1500)  # type: ignore
		print("GPU is compatible")
		return gpu_is_compatible

	def write_transcriptions_to_disk(
		self,
	):
		whisper_local = self
		for index, chunk in enumerate(whisper_local.speech_chunks):
			transcription_dir = whisper_local.transcription_dir
			# TODO - Sort the file name out using utils
			file_path = f"{transcription_dir}", f"{str(index)}-'''sort this''''.txt"

		return "Complete"

	def run_speech_to_text(self):
		whisper_local = self
		device = "cuda" if self.gpu_is_compatible() else "cpu"
		compute_type = "float16" if device == "cuda" else "int8"

		# Load faster-whisper model
		model = WhisperModel(
			whisper_local.chosen_whisper_model,
			device=device,
			compute_type=compute_type,  # type: ignore
		)
		chunks = whisper_local.speech_chunks

		for i, chunk in enumerate(tqdm(chunks, desc="Transcribing")):
			try:
				language = whisper_local.media_data.source_language  # type: ignore
				if language or language != "en":
					segments, info = model.transcribe(
						str(chunk.speech_chunk_path), language=language
					)
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
				warnings.warn(f"Unexpected error on chunk {i} ({chunk.speech_chunk_path}): {e}")
				chunk.transcribed_audio_text = "[ERROR: failed to transcribe]"

			finally:
				# Always set platform field, even on failure
				chunk.platform_transcribed_from = (
					f"Faster-Whisper-{whisper_local.chosen_whisper_model}"
				)

		return "Complete"

	@staticmethod
	def process_transcription_results(results_list, chunk: SpeechChunk):
		chunk_transcribed = []
		if len(results_list) > 1:
			for result in results_list:
				if result.text == "":
					warnings.warn(
						f"No transcription for {chunk.clip_srt_index}, will skip between {chunk.milisecond_start} and {chunk.milisecond_end} and continue"
					)
				else:
					chunk_transcribed.append(f"{chunk.clip_srt_index}: {result.text}")
		else:
			chunk_transcribed.append(results_list.text)

		return str(chunk_transcribed)


# whisper_local = WhisperLocal()
