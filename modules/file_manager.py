import os
from dataclasses import asdict
from pathlib import Path
from typing import List

from event_handlers_and_data.event_dispatchers import EventDispatchers
from pydub import AudioSegment

from data_classes.global_config import GlobalConfig
from data_classes.speech_chunk import SpeechChunk
from data_classes.state_steps import StateStep
from modules.utils import Utils


class FileManager:
    def __init__(self, global_config: GlobalConfig, utils: Utils) -> None:
        self.file
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

    def get_transcription_file_path(
        self, index_of_transcription
    ):  # could rework this to be universal but could get messy
        file_names = self.file_names
        # TODO - Check for a manager that takes care of updating the global config otherwise all objects are aiming to be frozen for safety
        transcription_file_name = Path(
            f"{index_of_transcription}{file_names.transcription_source_language_file_name}"
        ).with_suffix("txt")

        return transcription_file_name

        # TODO - Get the thing to join

    @staticmethod
    def write_speech_chunk_to_disk(
        segment: AudioSegment, chunk: SpeechChunk, chunk_file_path: Path
    ):
        segment.export(chunk_file_path, format=chunk.audio_format)
        chunk.speech_chunk_path = chunk_file_path
        print(f"Written speech chunk:{chunk_file_path}")

    @staticmethod
    def write_file_to_disk(content, file_path: Path):
        # This safely writes the file and flushes the buffer, avoids any issues with data hanging around that shouldn't.
        with open(file_path, "wb") as file:
            file.write(content)
            file.flush()
            os.fsync(file.fileno())

    def write_state_json_to_disk(self, state_step: StateStep, speech_chunks: List[SpeechChunk]):
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
