from data_classes.global_config import GlobalConfig
from data_classes.speech_chunk import SpeechChunk
from data_enums.compatible_audio_formats import CompatibleAudioFormats
from data_enums.compatible_video_formats import CompatibleVideoFormats
from data_enums.iso_639_languages import ISO639Language
from data_enums.iso_3166_regions import ISO3166Regions
from helper_functions.data.enum_evaluator import evaluate_enum


class MediaManager:
    def __init__(self, global_config: GlobalConfig):
        self.project_title = global_config.project_title

        # Video
        self.source_video_format = evaluate_enum(
            global_config.media_data.source_video_format, CompatibleVideoFormats
        )

        # Language
        self.source_language = evaluate_enum(
            global_config.media_data.source_language, ISO639Language
        )
        self.source_language_dialect = evaluate_enum(
            global_config.media_data.source_language_dialect, ISO3166Regions
        )
        self.target_language = evaluate_enum(
            global_config.media_data.target_language, ISO639Language
        )

        # Separate And Remove Audio Silence
        self.extracted_audio_format = evaluate_enum(
            global_config.media_data.extracted_audio_format, CompatibleAudioFormats
        )
        self.source_video_start_point = (
            global_config.audio_extraction_config.source_video_start_point
        )

        self.silence_removed_speech_chunks: list[SpeechChunk] = []

    def get_speech_chunks(self) -> list[SpeechChunk]:
        return self.silence_removed_speech_chunks
