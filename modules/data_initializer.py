from data_classes.global_config import (
    AppDirectories,
    AppPathsToFiles,
    AudioExtractionConfig,
    BaseFileNames,
    GlobalConfig,
    MediaData,
)
from data_classes.state_steps import state_steps
from data_enums.compatible_audio_formats import CompatibleAudioFormats
from data_enums.compatible_video_formats import CompatibleVideoFormats
from data_enums.iso_639_languages import ISO639Language
from data_enums.iso_3166_regions import ISO3166Regions
from data_enums.whisper_local_models import WhisperEnglishModels
from event_handlers_and_data.event_dispatchers import EventDispatchers
from event_handlers_and_data.event_handler import StatusData
from helper_functions.data.enum_evaluator import evaluate_enum
from modules.console_animator import ConsoleAnimator
from modules.utils import Utils


#########
########
class DataInitializer:
    def __init__(
        self, app_params, app_base_dir, utils: Utils, console_animator: ConsoleAnimator
    ):
        self.app_base_dir = app_base_dir
        self.app_params = app_params
        self.project_title = app_params.project_title
        self.whisper_local_chosen_model = app_params.whisper_local_chosen_model
        self.source_video_file_name = app_params.source_video_file_name
        self.global_config = ()
        self.utils = utils
        self.data_initializer_dispatcher = EventDispatchers.data_initializer_dispatcher
        self.add_listener = self.data_initializer_dispatcher.add_listener
        self.trigger_event = self.data_initializer_dispatcher.trigger_event

    def init_event_listeners(self):
        self.add_listener(self.on_global_config_completed)
        self.add_listener(self.on_global_config_failed)
        self.add_listener(self.on_app_paths_to_files_completed)
        self.add_listener(self.on_app_paths_to_files_failed)
        self.add_listener(self.on_app_directories_completed)
        self.add_listener(self.on_app_directories_failed)
        self.add_listener(self.on_media_data_completed)
        self.add_listener(self.on_media_data_failed)
        self.add_listener(self.on_audio_extraction_config_completed)
        self.add_listener(self.on_audio_extraction_config_failed)
        self.add_listener(self.on_base_file_names_completed)
        self.add_listener(self.on_base_file_names_failed)

    def get_global_config(self):
        data_initializer = self

        global_config = GlobalConfig(
            project_title=data_initializer.project_title,
            media_data=data_initializer.init_media_data(),
            audio_extraction_config=data_initializer.init_audio_extraction_config(),
            app_directories=data_initializer.init_app_directories(),
            base_file_names=data_initializer.init_base_file_names(),
            state_steps=state_steps,
            whisper_local_chosen_model=evaluate_enum(
                data_initializer.whisper_local_chosen_model, WhisperEnglishModels
            ),
            app_paths_to_files=data_initializer.init_app_paths_to_files(),
        )

        return global_config

    def init_app_paths_to_files(self):
        data_initializer = self

        video_file_path = self.utils.build_file_os_path(
                data_initializer.app_base_dir, data_initializer.source_video_file_name
            )
        
        app_paths_to_files = AppPathsToFiles(
            video_file_path=video_file_path,
            audio_from_video_path=None,
            transcription_source_language_paths=None,
            transcription_translated_language_dir=None,
        )
        
        

    def init_app_directories(self):
        data_initializer = self
        utils = self.utils
        app_base_dir = data_initializer.app_base_dir
        app_base_dir = utils.build_file_os_path(app_base_dir)
        project_folder_dir = utils.build_file_os_path(
            app_base_dir, data_initializer.project_title
        )

        app_directories = AppDirectories(
            app_base_dir=app_base_dir,
            project_folder_dir=project_folder_dir,
            extracted_audio_dir=utils.build_file_os_path(
                project_folder_dir, "extracted_audio"
            ),
            silence_removed_chunks_dir=utils.build_file_os_path(
                project_folder_dir, "silence_removed_audio"
            ),
            transcription_source_language_dir=utils.build_file_os_path(
                project_folder_dir, "transcription_source"
            ),
            transcription_translated_language_dir=utils.build_file_os_path(
                project_folder_dir, "transcription_translated"
            ),
            speech_chunk_json_dir=utils.build_file_os_path(
                project_folder_dir, data_initializer.project_title, "speech_chunk_data"
            ),
            global_config_json_dir=utils.build_file_os_path(
                project_folder_dir, data_initializer.project_title, "global_config_json"
            ),
            global_state_json_dir=utils.build_file_os_path(
                project_folder_dir, data_initializer.project_title, "global_state_json"
            ),
        )
        print(app_directories)
        return app_directories

    def init_media_data(self):
        app_params = self.app_params
        media_data = MediaData(
            extracted_audio_format=evaluate_enum(
                app_params.extracted_audio_format, CompatibleAudioFormats
            ),
            source_video_format=evaluate_enum(
                app_params.source_video_format, CompatibleVideoFormats
            ),
            target_language=evaluate_enum(app_params.target_language, ISO639Language),
            source_video_file_name=app_params.source_video_file_name,
            source_language=evaluate_enum(app_params.source_language, ISO639Language),
            source_language_dialect=evaluate_enum(
                app_params.source_language_dialect, ISO3166Regions
            ),
        )
        print(media_data)
        return media_data

    def init_audio_extraction_config(self):
        app_params = self.app_params
        audio_extraction_config = AudioExtractionConfig(
            source_video_start_point=app_params.source_video_start_point,
            user_silence_offset=app_params.user_silence_offset,
            user_silence_duration=app_params.user_silence_duration,
        )

        print(audio_extraction_config)
        return audio_extraction_config

    def init_base_file_names(self):
        app_params = self.app_params
        base_file_names = BaseFileNames(
            global_state_json_file_name=f"{app_params.project_title}-global-state-for-restore",
            transcription_source_language_file_name=f"{app_params.project_title}whisper-transcription-{app_params.source_language}",
            speech_chunk_json_file_name=f"{app_params.project_title}-speech-chunks-data",
            speech_chunk_audio_file_name=f"{app_params.project_title}-silence-removed-clip-",
            extracted_audio_file_name="extracted-from-video",
            transcription_text_filename="whisper-transcription",
            transcription_translated_text_filename=f"{app_params.project_title}-transcription-{app_params.source_language}",
            sub_source_language_file_name=f"{app_params.project_title}-subtitle-{app_params.source_language}",
            sub_target_language_file_name=f"source-language-sub-{app_params.source_video_file_name}-{app_params.source_language}-",
        )

        print(base_file_names)

    def on_global_config_completed(self, status_data: StatusData):
        print(status_data.status_message)
        # TODO: trigger next stage, e.g. self.init_app_paths_to_files()
        # EventDispatchers.data_initializer_dispatcher.trigger_event(
        #     DataInitializerEvents.APP_PATHS_TO_FILES_COMPLETED()
        # )

    def on_global_config_failed(self, status_data: StatusData):
        print(status_data.status_message)
        # TODO: handle error (rollback, retry, etc.)

    def on_app_paths_to_files_completed(self, status_data: StatusData):
        print(status_data.status_message)
        # TODO: trigger next stage, e.g. self.init_app_directories()

    def on_app_paths_to_files_failed(self, status_data: StatusData):
        print(status_data.status_message)

    def on_app_directories_completed(self, status_data: StatusData):
        print(status_data.status_message)
        # TODO: trigger next stage, e.g. self.init_media_data()

    def on_app_directories_failed(self, status_data: StatusData):
        print(status_data.status_message)

    def on_media_data_completed(self, status_data: StatusData):
        print(status_data.status_message)
        # TODO trigger next stage, e.g. self.init_audio_extraction_config()

    def on_media_data_failed(self, status_data: StatusData):
        print(status_data.status_message)

    def on_audio_extraction_config_completed(self, status_data: StatusData):
        print(status_data.status_message)
        # TODO: trigger next stage, e.g. self.init_base_file_names()

    def on_audio_extraction_config_failed(self, status_data: StatusData):
        print(status_data.status_message)

    def on_base_file_names_completed(self, status_data: StatusData):
        print(status_data.status_message)
        # TODO: trigger completion event
        # EventDispatchers.data_initializer_dispatcher.trigger_event(
        #     DataInitializerEvents.DATA_INITIALIZER_INIT_COMPLETED()
        # )

    def on_base_file_names_failed(self, status_data: StatusData):
        print(status_data.status_message)
