import os
from dataclasses import asdict
from pathlib import Path

from data_classes.global_config import GlobalConfig
from data_classes.speech_chunk import SpeechChunk
from data_classes.state_steps import StateStep


class FileManager:
	def __init__(self, directories: , utils: Utils) -> None:
		self.global_config = global_config
		self.utils = utils
		self.directories = global_config.app_directories
		self.app_base_dir = global_config.app_directories.app_base_dir
		self.source_video_path = global_config.app_paths_to_files.video_file_path
		self.file_names = global_config.base_file_names
		self.directories_have_been_built = False
		self.file_manager_dispatcher = EventDispatchers.file_manager_dispatcher
		self.add_listener = self.file_manager_dispatcher.add_listener
		self.trigger_event = self.file_manager_dispatcher.trigger_event

	@staticmethod
	def check_file_exists(file_path: Path):
		return os.path.isfile(str(file_path))

	@staticmethod
	def check_directroy_exists(directory: Path):
		path_to_string = str(directory)
		return os.path.exists(path_to_string) and os.path.isdir(path_to_string)

	# ****Using this one for now****
	def build_directories_in_file_system(self):
		directories = list(asdict(self.directories).values())
		# TODO - PUT AN EVENT LISTENER IN HERE FOR IF THE FILE EXISTS
		for directory in directories:
			directory.mkdir(parents=True, exist_ok=True)
			if self.check_directroy_exists(directory):
				print(f"{directory} built and ready")

		# TODO - Get the thing to join

	def write_state_json_to_disk(self, state_step: StateStep, speech_chunks: list[SpeechChunk]):
		file_manager = self
		speech_chunk_json_file_name = file_manager.utils.get_speech_chunk_json_file_name(state_step)

		speech_chunk_file_path = file_manager.build_file_os_path(
			file_manager.directories.speech_chunk_json_dir, speech_chunk_json_file_name
		).with_suffix(".json")

		state_step.state_step_file_path = speech_chunk_file_path
		state_step_jsonified = self.utils.convert_state_step_to_json(state_step=state_step)

		temp_path = file_manager.build_file_os_path(
			file_manager.directories.speech_chunk_json_dir, "temp"
		).with_suffix(".json")

		with open(temp_path, "w", encoding="utf-8") as file:
			file.write(state_step_jsonified)
			file.flush()
			os.fsync(file.fileno())
			os.replace(temp_path, state_step.state_step_file_path)

	def intit_event_listeners(self):
		self.add_lister()
