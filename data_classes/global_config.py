from dataclasses import dataclass
from pathlib import Path

from data_classes.state_steps import StateSteps
from data_enums.compatible_audio_formats import CompatibleAudioFormats
from data_enums.compatible_video_formats import CompatibleVideoFormats
from data_enums.iso_639_languages import ISO639Language
from data_enums.iso_3166_regions import ISO3166Regions
from data_enums.whisper_local_models import (
	WhisperEnglishModels,
	WhisperMultiLingualModels,
)


@dataclass
class AppDirectories:
	app_base_dir: Path
	project_folder_dir: Path
	extracted_audio_dir: Path
	silence_removed_chunks_dir: Path
	transcription_source_language_dir: Path
	transcription_translated_language_dir: Path
	speech_chunk_json_dir: Path
	global_config_json_dir: Path
	global_state_json_dir: Path


@dataclass
class AppPathsToFiles:
	video_file_path: Path
	audio_from_video_path: Path | None | None
	transcription_source_language_paths: list[Path] | None | None
	transcription_translated_language_dir: list[Path] | None | None


@dataclass
class AudioExtractionConfig:
	source_video_start_point: str
	user_silence_offset: int
	user_silence_duration: int


@dataclass
class MediaData:
	extracted_audio_format: str | CompatibleAudioFormats
	source_video_format: str | CompatibleVideoFormats
	target_language: str | ISO639Language
	source_video_file_name: str
	source_language: str | ISO639Language | None
	source_language_dialect: str | ISO3166Regions | None


@dataclass
class BaseFileNames:
	global_state_json_file_name: str
	transcription_source_language_file_name: str
	speech_chunk_audio_file_name: str
	speech_chunk_json_file_name: str
	extracted_audio_file_name: str
	transcription_text_filename: str
	transcription_translated_text_filename: str
	sub_source_language_file_name: str
	sub_target_language_file_name: str


@dataclass
class GlobalConfig:
	project_title: str
	media_data: MediaData | None
	audio_extraction_config: AudioExtractionConfig | None
	app_directories: AppDirectories | None
	base_file_names: BaseFileNames | None
	app_paths_to_files: AppPathsToFiles | None
	state_steps: StateSteps
	whisper_local_chosen_model: (
		str | WhisperMultiLingualModels | None | str | WhisperEnglishModels | None
	)
