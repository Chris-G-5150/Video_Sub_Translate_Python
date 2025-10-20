from dataclasses import dataclass
from pathlib import Path
from typing import Any, TypedDict

from data_types_and_classes.iso_639_languages import ISO639Language
from data_types_and_classes.iso_3166_regions import ISO3166Regions


class AppParams(TypedDict):
	project_title: str
	extracted_audio_format: str
	source_video_format: str
	target_language: str | ISO639Language
	source_video_file_name: str
	source_language: str | ISO639Language | None
	source_language_dialect: str | ISO3166Regions | None
	whisper_local_chosen_model: str
	source_video_start_point: str
	user_silence_offset: int
	user_silence_duration: int


@dataclass
class StateStep:
	step_name: str
	description: str
	speech_chunks_file_path: Path | None = None
	state_step_file_path: Path | None = None
	completion_status: str | None = None
	state_written_to_disk: bool = False


@dataclass
class SpeechChunk:
	project_title: str
	clip_srt_index: int
	speech_chunk_path: Path
	millisecond_start: int
	millisecond_end: int
	duration_in_milliseconds: int
	audio_format: str
	source_language: str
	transcription_file_path: Path | None
	transcription_source_language_path: Path | None
	transcription_target_language_path: Path | None
	transcription_source_language_text: str | None
	transcription_target_language_text: str | None


@dataclass
class Injectable(TypedDict):
	name: str
	category: str
	payload: Any
