import json
import os
import shutil
from dataclasses import dataclass, asdict
from pathlib import Path
from pydub import AudioSegment
from data_classes.speech_chunk import SpeechChunk
from typing import TYPE_CHECKING

from data_classes.state_steps import StateStep, state_steps
from modules.media_manager import MediaManager

if TYPE_CHECKING:
    from module_parameters.app_params import AppParams

@dataclass
class BuildDirectories:
    app_base_dir: Path
    video_file_path: Path
    project_folder_dir: Path
    extracted_audio_dir: Path  # removed slash because of extract audio in pydub not liking it, the rest us OS
    silence_removed_chunks_dir: Path
    transcription_source_language_dir: Path
    transcription_translated_language_dir: Path
    speech_chunk_json_dir: Path


class FileManager:
    def __init__(self, app_params: "AppParams", media_manager: MediaManager, app_base_dir: Path | None, directories = None) -> None:
        self.app_params = app_params
        self.media_manager = media_manager
        self.directories = directories
        self.app_base_dir = app_base_dir
        self.state_steps = state_steps
        self.extracted_audio_path = None

    @staticmethod
    def check_file_exists(file_path:str):
        return os.path.isfile(file_path)

    @staticmethod
    def check_directroy_exists(directory):
        return os.path.exists(directory) and os.path.isdir(directory)

    def build_file_os_path(self, *parts: str | Path) -> Path:
        base_dir = self.app_base_dir
        return base_dir.joinpath(*parts)

    def set_directory_paths_in_file_manager(self):
        app_params = self.app_params
        source_video_file_name = app_params.source_video_file_name
        self.directories = self.build_directory_paths(project_title=app_params.project_title, source_video_file_name=source_video_file_name)

    def build_directories_in_file_system(self):
        directories = list(asdict(self.directories).values())
        file_manager = self
        video_path = Path(file_manager.directories.video_file_path)
        directories.remove(video_path)

        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
            if self.check_directroy_exists(directory):
                print(f"{directory} built and ready")

    def build_directory_paths(self, project_title: str, source_video_file_name: str):
        app_base_dir = self.app_base_dir
        video_file_path = self.build_file_os_path(app_base_dir, source_video_file_name)
        project_dir = self.build_file_os_path(app_base_dir, project_title)
        extracted_audio_dir = self.build_file_os_path(project_dir, 'extracted_audio')
        silence_removed_chunks_dir = self.build_file_os_path(project_dir, 'silence_removed_audio')
        transcription_source_dir = self.build_file_os_path(project_dir, 'transcription_source')
        transcription_translated_dir = self.build_file_os_path(project_dir, 'transcription_translated')
        speech_chunk_json_dir = self.build_file_os_path(app_base_dir, project_title, 'speech_chunk_data')

        build_directories = BuildDirectories(
            app_base_dir=app_base_dir,
            video_file_path=video_file_path,
            project_folder_dir=project_dir,
            extracted_audio_dir=extracted_audio_dir,
            silence_removed_chunks_dir=silence_removed_chunks_dir,
            transcription_source_language_dir=transcription_source_dir,
            transcription_translated_language_dir=transcription_translated_dir,
            speech_chunk_json_dir=speech_chunk_json_dir
        )

        return build_directories

    def build_directory(self, directory: str):
        # check for dir existing
        if self.check_directroy_exists(directory):
            # deletes dir if exists
            shutil.rmtree(directory)
        # rebuilds dir
        Path(directory).mkdir(parents=True, exist_ok=True)

    def build_transcription_file_name(self, index_of_transcription, ): # could rework this to be universal but could get messy
        app_params = self.app_params
        return f"{index_of_transcription}-{app_params.project_title}-{app_params.source_language}-transcription"

    @staticmethod
    def write_speech_chunk_to_disk(segment: AudioSegment, chunk: SpeechChunk, chunk_file_path: Path):
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

    @staticmethod
    def convert_state_to_json(state_step: StateStep) -> str:
        return json.dumps(state_step, indent=4)

    def write_state_json_to_disk(self, state_step: StateStep, speech_chunks: list[SpeechChunk]):
        file_manager = self
        speech_chunk_json_file_name = f"{state_step.step}-{file_manager.app_params.project_title}-{state_step.step}"

        temp_path = file_manager.build_file_os_path(file_manager.directories.speech_chunk_json_dir, 'temp').with_suffix(".json")
        finished_file_path = file_manager.build_file_os_path(file_manager.directories.speech_chunk_json_dir, speech_chunk_json_file_name).with_suffix(".json")

        state_step.speech_chunks = speech_chunks
        state_step.speech_chunks_file_path = finished_file_path

        with open(temp_path, "wb", encoding='utf-8') as file:
            file_manager.convert_state_to_json(state_step)
            file.flush()
            os.fsync(file.fileno())
            os.replace(temp_path, finished_file_path)

    # Gets ran on app start to see how far in the process the app was along last time it was run.
    # Checks folders for existing json files, so will check each json directory, will then work out
    # where to start again based on if the folder has content, load the speech chunks which contain
    # all the relevant data that the program needs to run.

    def process_point_check(self):
        file_manager = self
        directories = file_manager.directories
        app_base_dir = directories.app_base_dir
        json_dir = directories.speech_chunk_json_dir
        extracted_audio_dir = directories.extracted_audio_dir

        directories_to_check = [app_base_dir, json_dir, extracted_audio_dir]

        for directory in directories_to_check:
            match directory:
                case json_dir:
                    # TODO - finish this set of checks will make testing faster in the longrun


























