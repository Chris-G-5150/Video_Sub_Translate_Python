from dataclasses import dataclass
from pathlib import Path
from typing import TypedDict

from data_types_and_classes.iso_639_languages import ISO639Language
from data_types_and_classes.iso_3166_regions import ISO3166Regions


@dataclass
class SpeechChunk:
	def __init__(
		self,
		project_title: str,
		clip_srt_index: int,
		speech_chunk_path: Path,
		milisecond_start: int,
		milisecond_end: int,
		duration_in_miliseconds: int,
		audio_format: str,
		source_language: str,
		transcription_file_path: Path | None = None,
		transcription_source_language_path: Path | None = None,
		transcription_target_language_path: Path | None = None,
		transcription_source_language_text: str | None = None,
		transcription_target_language_text: str | None = None,
	):
		self.project_title = project_title
		self.clip_srt_index = clip_srt_index
		self.speech_chunk_path = speech_chunk_path
		self.milisecond_start = milisecond_start
		self.milisecond_end = milisecond_end
		self.duration_in_miliseconds = duration_in_miliseconds
		self.audio_format = audio_format
		self.source_language = source_language
		self.transcription_file_path = transcription_file_path
		self.transcription_source_language_path = transcription_source_language_path
		self.transcription_target_language_path = transcription_target_language_path
		self.transcription_source_language_text = transcription_source_language_text
		self.transcription_target_language_text = transcription_target_language_text


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


# def build_speech_chunk_dict(
# 	project_title: str,
# 	clip_srt_index: int,
# 	speech_chunk_path: Path,
# 	milisecond_start: int,
# 	milisecond_end: int,
# 	duration_in_miliseconds: int,
# 	audio_format: str,
# 	source_language: str,
# 	transcription_file_path: Path | None,
# 	transcription_source_language_path: Path | None,
# 	transcription_target_language_path: Path | None,
# 	transcription_source_language_text: str | None,
# 	transcription_target_language_text: str | None,
# ):
# 	return {
# 		project_title,
# 		clip_srt_index,
# 		speech_chunk_path,
# 		milisecond_start,
# 		milisecond_end,
# 		duration_in_miliseconds,
# 		audio_format,
# 		source_language,
# 		transcription_file_path,
# 		transcription_source_language_path,
# 		transcription_target_language_path,
# 		transcription_source_language_text,
# 		transcription_target_language_text,
# 	}
