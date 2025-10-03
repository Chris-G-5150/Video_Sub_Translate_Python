from typing import TYPE_CHECKING

from data_enums.compatible_audio_formats import CompatibleAudioFormats
from data_enums.compatible_video_formats import CompatibleVideoFormats
from data_enums.iso_3166_regions import ISO3166Regions
from data_enums.iso_639_languages import ISO639Language

from helper_functions.enum_evaluator import evaluate_enum
from module_parameters.media_manager_params import MediaManagerParams
from data_classes.speech_chunk import SpeechChunk

if TYPE_CHECKING:
    from module_parameters.app_params import AppParams

class MediaManager:
    def __init__(self, media_manager_params: MediaManagerParams, app_params: "AppParams"):
        self.project_title = app_params.project_title
        # Video
        self.source_video_format = evaluate_enum(app_params.source_video_format, CompatibleVideoFormats)
        # Language
        self.source_language = evaluate_enum(app_params.source_language, ISO639Language)
        self.source_language_dialect = evaluate_enum(app_params.source_language_dialect, ISO3166Regions)
        self.target_language = evaluate_enum(app_params.target_language, ISO639Language)
        # Separate And Remove Audio Silence
        self.silence_removed_speech_chunks: list[SpeechChunk] = []
        self.extracted_audio_format = evaluate_enum(app_params.extracted_audio_format, CompatibleAudioFormats)
        self.source_video_start_point = media_manager_params.source_video_start_point
        self.user_silence_offset = media_manager_params.user_silence_offset
        self.user_silence_duration = media_manager_params.user_silence_duration

    def add_speech_chunk(self, speech_chunk: SpeechChunk):
        self.silence_removed_speech_chunks.append(speech_chunk)

    def get_speech_chunks(self) -> list[SpeechChunk]:
        return self.silence_removed_speech_chunks

    def get_source_language(self) -> str:
        return str(self.source_language)

    def clear_speech_chunks(self):
        self.silence_removed_speech_chunks= []



















