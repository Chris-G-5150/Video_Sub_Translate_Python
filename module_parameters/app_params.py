from dataclasses import dataclass
from typing import Optional

from data_enums.compatible_audio_formats import CompatibleAudioFormats
from data_enums.compatible_video_formats import CompatibleVideoFormats
from data_enums.iso_639_languages import ISO639Language
from data_enums.iso_3166_regions import ISO3166Regions
from data_enums.whisper_local_models import (
    WhisperEnglishModels,
    WhisperMultiLingualModels,
)


@dataclass
class AppParams:
    project_title: str
    extracted_audio_format: str | CompatibleAudioFormats
    source_video_format: str | CompatibleVideoFormats
    target_language: str | ISO639Language
    source_video_file_name: str
    source_language: Optional[str | ISO639Language]
    source_language_dialect: Optional[str | ISO3166Regions]
    whisper_local_chosen_model: (
        Optional[str | WhisperMultiLingualModels] | Optional[str | WhisperEnglishModels]
    )
    target_language: Optional[str | ISO639Language]
    source_video_start_point: str = "00:00:00"
    user_silence_offset: int = 15
    user_silence_duration: int = 1500
