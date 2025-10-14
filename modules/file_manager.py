import os
from dataclasses import asdict
from pathlib import Path

from pydub import AudioSegment

from data_types_and_classes.data_constants import CompatibleAudioFormats, CompatibleVideoFormats
from data_types_and_classes.data_types import SpeechChunk
from data_types_and_classes.iso_639_languages import ISO639Language
from data_types_and_classes.iso_3166_regions import ISO3166Regions
from helper_classes import DotDict

"""
FileManager- this will be an app wide class, will get initialized when the app first starts. 

Since building directories is only used once, is put in a separate class 
to be automated on app start, this is just for it to work with automation system

Params:
	file_paths: Will be referenced by global_config, class won't be initialized until this is done anyway, 
	will find a way to work around this, 

	file_names: Will be referenced through global_config, there will be a separate class that takes care of 
	creating all the file names when they are needed. This will pretty much just be a loop that adds an index
	and a state step so the exact time the file was created will be clear, more than likely managed by GlobalStateManager.

	Not sure on how correct my thinking is but will have a separate class for building all the JSON files on each step,
	may add directories for each state step so files don't get lost or hard to find all in one place. 
"""


class FileManager:
	def __init__(self, app_params, global_config, app_base_dir: Path):
		self.app_params = app_params
		self.file_paths = global_config.app_paths_to_files
		self.file_names = global_config.base_file_names
		self.directories = global_config.app_directories
		self.app_base_dir = app_base_dir

	@staticmethod
	def check_file_exists(file_path: Path):
		return os.path.isfile(str(file_path))

	@staticmethod
	def check_directroy_exists(directory: Path):
		path_to_string = str(directory)
		return os.path.exists(path_to_string) and os.path.isdir(path_to_string)

	def build_file_os_path(self, *parts: str | Path) -> Path:
		return self.app_base_dir.joinpath(*parts)

	@staticmethod
	def write_file_to_disk(content, file_path: Path):
		# This safely writes the file and flushes the buffer, avoids any issues with data hanging around that shouldn't.
		with open(file_path, "wb") as file:
			file.write(content)
			file.flush()
			os.fsync(file.fileno())

	@staticmethod
	def write_speech_chunk_to_disk(
		segment: AudioSegment, chunk: SpeechChunk, chunk_file_path: Path
	):
		segment.export(chunk_file_path, format=chunk.audio_format)
		chunk.speech_chunk_path = chunk_file_path
		print(f"Written speech chunk:{chunk_file_path}")

	@staticmethod
	def build_transcription_file_path(
		transcription_dir: Path,
		base_transcription_file_name: Path | str,
		index_of_transcription: int,
	):
		assert transcription_dir is not None
		filename = f"{index_of_transcription}-{base_transcription_file_name}"
		return transcription_dir.joinpath(filename).with_suffix("txt")

	def build_directories_in_file_system(self):
		assert self.directories is not None

		directories = list(asdict(self.directories).values())

		for directory in directories:
			directory.mkdir(parents=True, exist_ok=True)
			if self.check_directroy_exists(directory):
				print(f"{directory} built and ready")

	# ==============================================================================
	# Since typing and imports have been less than useful just putting all the data initializer as functions in this class
	# ==============================================================================
	# def build_global_config(self, app_params, app_base_dir):
	# 	return self.build_global_config_dict(
	# 			project_title =
	# 			media_data =
	# 			audio_extraction_config =
	# 			app_directories =
	# 			base_file_names =
	# 			app_paths_to_files =
	# 			whisper_local_chosen_model =
	# 		)

	def build_global_config(self):
		project_title = self.app_params.project_title
		media_data = self.init_media_data()
		audio_extraction_config = self.init_audio_extraction_config()
		app_directories = self.init_app_directories()
		base_file_names = self.init_base_file_names()
		app_paths_to_files = self.init_app_paths_to_files()
		whisper_local_chosen_model = self.app_params.whisper_local_chosen_model

		self.global_config = DotDict({
			"project_title": project_title,
			"media_data": media_data,
			"audio_extraction_config": audio_extraction_config,
			"app_directories": app_directories,
			"base_file_names": base_file_names,
			"app_paths_to_files": app_paths_to_files,
			"whisper_local_chosen_model": whisper_local_chosen_model,
		})

	def init_app_paths_to_files(self):
		return self.build_app_paths_to_files_dict(
			video_file_path=self.build_file_os_path(
				self.app_base_dir, self.app_params.source_video_file_name
			),
			audio_from_video_path=None,
			transcription_source_language_paths=None,
			transcription_translated_language_dir=None,
		)

	def init_app_directories(self):
		# put all of these files in file manager.
		app_base_dir = self.app_base_dir
		project_folder_dir = self.build_file_os_path(app_base_dir, self.app_params.project_title)

		return self.build_app_directories_dict(
			app_base_dir=app_base_dir,
			project_folder_dir=project_folder_dir,
			extracted_audio_dir=self.build_file_os_path(project_folder_dir, "extracted_audio"),
			silence_removed_chunks_dir=self.build_file_os_path(
				project_folder_dir, "silence_removed_audio"
			),
			transcription_source_language_dir=self.build_file_os_path(
				project_folder_dir, "transcription_source"
			),
			transcription_translated_language_dir=self.build_file_os_path(
				project_folder_dir, "transcription_translated"
			),
			speech_chunk_json_dir=self.build_file_os_path(
				project_folder_dir, self.app_params.project_title, "speech_chunk_data"
			),
			global_config_json_dir=self.build_file_os_path(
				project_folder_dir, self.app_params.project_title, "global_config_json"
			),
			global_state_json_dir=self.build_file_os_path(
				project_folder_dir, self.app_params.project_title, "global_state_json"
			),
		)

	def init_media_data(self):
		return self.build_media_data_dict(
			extracted_audio_format=CompatibleAudioFormats[
				f"{self.app_params.extracted_audio_format}"
			],
			source_video_format=CompatibleVideoFormats[f"{self.app_params.source_video_format}"],
			target_language=f"{self.app_params.target_language}",
			source_video_file_name=self.app_params.source_video_file_name,
			source_language=evaluate_enum(self.app_params.source_language, ISO639Language),
			source_language_dialect=evaluate_enum(
				self.app_params.source_language_dialect, ISO3166Regions
			),
		)

	def init_audio_extraction_config(self):
		return self.build_audio_extraction_config_dict(
			source_video_start_point=self.app_params.source_video_start_point,
			user_silence_offset=self.app_params.user_silence_offset,
			user_silence_duration=self.app_params.user_silence_duration,
		)

	def init_base_file_names(self):
		return self.build_base_file_names_dict(
			global_state_json_file_name=f"{self.app_params.project_title}-global-state-for-restore",
			transcription_source_language_file_name=f"{self.app_params.project_title}whisper-transcription-{self.app_params.source_language}",
			speech_chunk_json_file_name=f"{self.app_params.project_title}-speech-chunks-data",
			speech_chunk_audio_file_name=f"{self.app_params.project_title}-silence-removed-clip-",
			extracted_audio_file_name=f"{self.app_params.project_title}-extracted-from-video",
			transcription_text_filename=f"{self.app_params.project_title}-whisper-transcription",
			transcription_translated_text_filename=f"{self.app_params.project_title}-transcription-{self.app_params.source_language}",
			sub_source_language_file_name=f"{self.app_params.project_title}-subtitle-{self.app_params.source_language}",
			sub_target_language_file_name=f"{self.app_params.project_title}-subtitle-{self.app_params.target_language}-{self.app_params.source_language}",
		)

	@staticmethod
	def build_app_directories_dict(
		app_base_dir: Path,
		project_folder_dir: Path,
		extracted_audio_dir: Path,
		silence_removed_chunks_dir: Path,
		transcription_source_language_dir: Path,
		transcription_translated_language_dir: Path,
		speech_chunk_json_dir: Path,
		global_config_json_dir: Path,
		global_state_json_dir: Path,
	):
		return {
			app_base_dir,
			project_folder_dir,
			extracted_audio_dir,
			silence_removed_chunks_dir,
			transcription_source_language_dir,
			transcription_translated_language_dir,
			speech_chunk_json_dir,
			global_config_json_dir,
			global_state_json_dir,
		}

	@staticmethod
	def build_app_paths_to_files_dict(
		video_file_path: Path | None,
		audio_from_video_path: Path | None,
		transcription_source_language_paths: Path | None,
		transcription_translated_language_dir: Path | None,
	):
		return {
			video_file_path,
			audio_from_video_path,
			transcription_source_language_paths,
			transcription_translated_language_dir,
		}

	@staticmethod
	def build_audio_extraction_config_dict(
		source_video_start_point: str, user_silence_offset: int, user_silence_duration: int
	):
		return {
			source_video_start_point,
			user_silence_offset,
			user_silence_duration,
		}

	@staticmethod
	def build_media_data_dict(
		extracted_audio_format: str,
		source_video_format: str,
		target_language: str,
		source_video_file_name: str,
		source_language: str,
		source_language_dialect: str,
	):
		return {
			extracted_audio_format,
			source_video_format,
			target_language,
			source_video_file_name,
			source_language,
			source_language_dialect,
		}

	@staticmethod
	def build_base_file_names_dict(
		global_state_json_file_name,
		transcription_source_language_file_name,
		speech_chunk_audio_file_name,
		speech_chunk_json_file_name,
		extracted_audio_file_name,
		transcription_text_filename,
		transcription_translated_text_filename,
		sub_source_language_file_name,
		sub_target_language_file_name,
	):
		return {
			global_state_json_file_name,
			transcription_source_language_file_name,
			speech_chunk_audio_file_name,
			speech_chunk_json_file_name,
			extracted_audio_file_name,
			transcription_text_filename,
			transcription_translated_text_filename,
			sub_source_language_file_name,
			sub_target_language_file_name,
		}

	@staticmethod
	def build_global_config_dict(
		project_title,
		media_data,
		audio_extraction_config,
		app_directories,
		base_file_names,
		app_paths_to_files,
		whisper_local_chosen_model,
	):
		return {
			project_title,
			media_data,
			audio_extraction_config,
			app_directories,
			base_file_names,
			app_paths_to_files,
			whisper_local_chosen_model,
			base_file_names,
		}
