from data_classes.class_event_list_item import ClassEventListItem
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
from debug_tools.debug_printer import printer  # type: ignore
from helper_functions.data.enum_evaluator import evaluate_enum
from module_parameters.app_params import AppParams
from modules.console_animator import ConsoleAnimator
from modules.utils import Utils


class DataInitializer:
	def __init__(
		self,
		app_params: AppParams,
		app_base_dir: str,
		utils: Utils,
		console_animator: ConsoleAnimator,
	):
		self.app_base_dir = app_base_dir
		self.app_params = app_params
		self.project_title = app_params.project_title
		self.whisper_local_chosen_model = app_params.whisper_local_chosen_model
		self.source_video_file_name = app_params.source_video_file_name
		self.global_config = None | GlobalConfig
		self.media_data = None
		self.audio_extraction = None
		self.app_directories = None
		self.base_file_names = None
		self.app_paths_to_files = None
		self.utils = utils
		self.events_list = self.get_events_list

	def build_global_config(self):
		data_initializer = self
		global_config = GlobalConfig(
			project_title=data_initializer.project_title,
			media_data=self.media_data,
			audio_extraction_config=self.audio_extraction_config,
			app_directories=self.app_directories,
			base_file_names=self.base_file_names,
			state_steps=state_steps,
			whisper_local_chosen_model=evaluate_enum(
				data_initializer.whisper_local_chosen_model,
				WhisperEnglishModels,
			),
			app_paths_to_files=data_initializer.init_app_paths_to_files(),
		)
		printer(global_config)
		self.global_config = global_config

	def init_app_paths_to_files(self):
		data_initializer = self
		app_base_dir = data_initializer.app_base_dir
		self.app_paths_to_files = AppPathsToFiles(
			video_file_path=self.utils.build_file_os_path(
				app_base_dir, data_initializer.source_video_file_name
			),
			audio_from_video_path=None,
			transcription_source_language_paths=None,
			transcription_translated_language_dir=None,
		)

	def init_app_directories(self):
		data_initializer = self
		utils = self.utils
		app_base_dir = data_initializer.app_base_dir
		app_base_dir = utils.build_file_os_path(app_base_dir)
		project_folder_dir = utils.build_file_os_path(app_base_dir, data_initializer.project_title)

		self.app_directories = AppDirectories(
			app_base_dir=app_base_dir,
			project_folder_dir=project_folder_dir,
			extracted_audio_dir=utils.build_file_os_path(project_folder_dir, "extracted_audio"),
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

	def init_media_data(self):
		app_params = self.app_params
		self.media_data = MediaData(
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

	def init_audio_extraction_config(self):
		app_params = self.app_params
		self.audio_extraction = AudioExtractionConfig(
			source_video_start_point=app_params.source_video_start_point,
			user_silence_offset=app_params.user_silence_offset,
			user_silence_duration=app_params.user_silence_duration,
		)

	def init_base_file_names(self):
		app_params = self.app_params
		self.base_file_names = BaseFileNames(
			global_state_json_file_name=f"{app_params.project_title}-global-state-for-restore",
			transcription_source_language_file_name=f"{app_params.project_title}whisper-transcription-{app_params.source_language}",
			speech_chunk_json_file_name=f"{app_params.project_title}-speech-chunks-data",
			speech_chunk_audio_file_name=f"{app_params.project_title}-silence-removed-clip-",
			extracted_audio_file_name=f"{app_params.project_title}-extracted-from-video",
			transcription_text_filename=f"{app_params.project_title}-whisper-transcription",
			transcription_translated_text_filename=f"{app_params.project_title}-transcription-{app_params.source_language}",
			sub_source_language_file_name=f"{app_params.project_title}-subtitle-{app_params.source_language}",
			sub_target_language_file_name=f"{app_params.project_title}-subtitle-{app_params.target_language}-{app_params.source_language}",
		)

	def get_events_list(self):
		return [
			ClassEventListItem(
				order=1,
				event_name="global_config_media_data",
				class_ref=self,
				function_ref=self.init_media_data,
			),
			ClassEventListItem(
				order=2,
				event_name="global_config_audio_extraction_config",
				class_ref=self,
				function_ref=self.init_audio_extraction_config,
			),
			ClassEventListItem(
				order=3,
				event_name="global_config_app_directories",
				class_ref=self,
				function_ref=self.init_app_directories,
			),
			ClassEventListItem(
				order=4,
				event_name="global_config_base_file_names",
				class_ref=self,
				function_ref=self.init_app_directories,
			),
			ClassEventListItem(
				order=5,
				event_name="global_config_app_paths_to_files",
				class_ref=self,
				function_ref=self.init_app_paths_to_files,
			),
			ClassEventListItem(
				order=6,
				event_name="global_config_create_global_config",
				class_ref=self,
				function_ref=self.build_global_config,
			),
		]
