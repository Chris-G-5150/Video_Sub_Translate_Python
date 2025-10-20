import sys
from pathlib import Path

from data_types_and_classes.data_types import AppParams
from data_types_and_classes.iso_639_languages import ISO639Language
from data_types_and_classes.iso_3166_regions import ISO3166Regions
from modules.console_animator import ConsoleAnimator
from modules.global_state_manager import GlobalStateManager

ROOT_DIR = Path(__file__).resolve().parent
if str(ROOT_DIR) not in sys.path:
	sys.path.insert(0, str(ROOT_DIR))

BASE_DIRECTORY = Path(__file__).resolve().parent


# GLOBAL DEBUGGER DISABLED IF ENV NOT SET CORRECTLY###################################
# not included in git repo nor is the debugger itself
# GLOBAL DEBUGGER DISABLED IF ENV NOT SET CORRECTLY###################################


class App:
	def __init__(
		self,
		app_params: AppParams,
		# type: ignore
	):
		# Classes that take care of each part of the project
		self.app_params = app_params
		self.console_animator = ConsoleAnimator()
		self.app_base_directory = BASE_DIRECTORY
		self.project_title = self.app_params.project_title
		# self.utils = Utils(BASE_DIRECTORY)
		self.global_state_manager: GlobalStateManager | None = None
		# intializers
		self.json_utilities = None
		self.global_config = None
		# classes
		self.separate_audio_from_video = None
		self.separate_and_remove_audio_silience = None
		self.speech_to_text_generator = None
		self.sub_title_file_generator = None
		self.wisper_local = None
		# events system

	def init(self):
		self.global_state_manager = GlobalStateManager(
			app_base_dir=BASE_DIRECTORY,
			app_params=self.app_params,
			console_animator=self.console_animator,
		)

	def on_global_state_manager_init(self, event_data: StatusData):
		if event_data.status == EventStatus.OK and self.global_state_manager:
			self.global_state_manager.init()
		else:
			"Global State Manager Failed"


test_app_params = AppParams(
	project_title="test",
	extracted_audio_format=CompatibleAudioFormats.MP3,
	source_video_file_name="coronationstreet.mp4",
	target_language=ISO639Language.Spanish,
	source_video_format=CompatibleVideoFormats.MP4,
	source_language=ISO639Language.English,
	source_language_dialect=ISO3166Regions.UnitedKingdom,
	whisper_local_chosen_model=WhisperEnglishModels.BaseEn,
)


application = App(test_app_params).init()
