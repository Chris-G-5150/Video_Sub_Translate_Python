import os
from dataclasses import asdict
from pathlib import Path

from pydub import AudioSegment

from data_types_and_classes.data_types import SpeechChunk

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
	def __init__(self, app_params, app_base_dir):
		self.app_base_dir = app_base_dir
		self.app_params = app_params

	@staticmethod
	def check_file_exists(file_path: Path):
		return os.path.isfile(str(file_path))

	@staticmethod
	def check_directory_exists(directory: Path):
		path_to_string = str(directory)
		return os.path.exists(path_to_string) and os.path.isdir(path_to_string)

	@staticmethod
	def build_file_os_path(app_base_dir, *parts: str | Path) -> Path:
		return app_base_dir.joinpath(*parts)

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

	def build_directories_in_file_system(self, global_config: GlobalConfig):
		assert global_config.directories is not None

		directories = list(asdict(self.).values())

		for directory in directories:
			directory.mkdir(parents=True, exist_ok=True)
			if self.check_directory_exists(directory):
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
