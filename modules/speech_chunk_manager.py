# from typing import Optional
# from data_classes.global_config import GlobalConfig
# from data_classes.speech_chunk import SpeechChunk
#
# class SpeechChunkManager:
#     def __init__(self, global_config: GlobalConfig):
#         self.global_config = global_config
#         self.source_audio_path = global_config.app_directories.extracted_audio_dir
#         self.speech_chunk_path = global_config.app_directories.silence_removed_chunks_dir
#         self.speech_chunk_audio_format = global_config.media_data.extracted_audio_format
#         self.speech_chunk_source_language = global_config.media_data.source_language
#         self.speech_chunk_target_language = global_config.media_data.target_language
#         self.transcription_source_language_path = global_config.app_directories.transcription_source_language_dir
#         self.transcription_target_language_path = global_config.app_directories.transcription_translated_language_dir
#         self._speech_chunks: list[SpeechChunk] | None = None
#
#         def get_speech_chunks() -> Optional[list[SpeechChunk]]:
#             return self._speech_chunks
#
#         def add_speech_chunk(speech_chunk: SpeechChunk):
#             self._speech_chunks.append(speech_chunk)
#
#         def update_speech_chunks(self, property: str, value: str | Path):
#             # TODO - finish tomorrow
#
#
