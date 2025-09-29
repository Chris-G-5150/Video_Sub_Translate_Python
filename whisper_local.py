import whisper
import GPUtil
import speech_chunk
import warnings

# model = whisper.load_model("turbo")
# result = model.transcribe("audio.mp3")
# print(result["text"])

class WhisperLocal:
    def __init__(
            self,
            speech_chunks: list[speech_chunk.SpeechChunk],
            user_set_language = None
    ):
        self.detected_language = None
        self.speech_chunks = speech_chunks
        self.user_set_language = user_set_language
        self.available_models_multilingual = ["tiny", "base", "small", "medium", "large", "turbo"]
        self.available_models_english = ["tiny.en", "base.en", "small.en", "medium.en"]
        self.chosen_model = None
        self.video_card_details = GPUtil.getGPUs()

    def set_chosen_model(self, chosen_model):
        self.chosen_model = chosen_model

    def clear_chosen_model(self):
        self.chosen_model = None

    def gpu_is_compatible(self) -> bool:
        gpu = self.video_card_details
        return bool(gpu and gpu[0].memoryTotal >= 1500)

    def run_speech_to_text(self):
        if self.gpu_is_compatible():
            model = whisper.load_model(self.chosen_model)

            if hasattr(self, "user_set_language"):
                for chunk in self.speech_chunks:
                    audio = whisper.load_audio(chunk.path_to_clip)
                    mel = whisper.log_mel_spectrogram(audio, n_mels=model.dims.n_mels).to(model.device)
                    options = whisper.DecodingOptions(language=self.user_set_language)
                    results = whisper.decode(model, mel, options)
                    chunk.transcribed_audio = self.process_transcription_results(self, results, chunk)

            else:
                for chunk in self.speech_chunks:
                    mel = whisper.log_mel_spectrogram(chunk.path_to_clip, n_mels=model.dims.n_mels).to(model.device)
                    _, probs = model.detect_language(mel)
                    options = whisper.DecodingOptions()
                    results = whisper.decode(model, mel, options)

    @staticmethod
    def process_transcription_results(self, results_list, chunk):
        chunk_transcribed = []
        if len(results_list) > 1:
            for result in results_list:
                if result.text == "":
                    warnings.warn(
                        f"No transcription for {chunk.clip_srt_index}, will skip between {chunk.time_stamp_start} and {chunk.time_stamp_end} and continue")
                else:
                    chunk_transcribed.append(result.text + " ")
        else:
            chunk_transcribed.append(results_list.text)

        return str(chunk_transcribed)


 # whisper_local = WhisperLocal()

