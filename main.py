from pathlib import Path

from data_classes.global_config import GlobalConfig
from data_enums.compatible_audio_formats import CompatibleAudioFormats
from data_enums.compatible_video_formats import CompatibleVideoFormats
from data_enums.iso_639_languages import ISO639Language
from data_enums.iso_3166_regions import ISO3166Regions
from data_enums.whisper_local_models import WhisperEnglishModels
from event_handlers_and_data.event_handler import EventHandler
from module_parameters.app_params import AppParams
from modules.console_animator import ConsoleAnimator
from modules.global_state_manager import GlobalStateManager
from modules.utils import Utils

BASE_DIRECTORY = Path(__file__).resolve().parent


###############################GLOBAL DEBUGGER DISABLED IF ENV NOT SET CORRECTLY###################################
# not included in git repo nor is the debugger itself
###############################GLOBAL DEBUGGER DISABLED IF ENV NOT SET CORRECTLY###################################


class App:
    def __init__(
        self,
        app_params: AppParams,
        app_event_dispatcher: EventHandler | None = None,
    ):
        # event_handler_global
        self.app_event_dispatcher = app_event_dispatcher
        # Classes that take care of each part of the project
        self.app_params = app_params
        self.console_animator = ConsoleAnimator()
        self.app_base_directory = BASE_DIRECTORY
        self.project_title = self.app_params.project_title
        self.utils = Utils(BASE_DIRECTORY)
        self.global_config = GlobalConfig | None
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

    def init(self) -> None:
        app = self

        self.global_state_manager = GlobalStateManager(
            app_base_dir=BASE_DIRECTORY,
            app_params=app.app_params,
            utils=app.utils,
            global_config=None,
            console_animator=app.console_animator,
            global_state_dispatcher=None,
        )

        self.global_state_manager.init_event_listeners()
        # TODO - Add global event dispatcher to init on GlobalStateManager

        # Then, once init has completed.
        # 1. Check to see  if project folder exists
        # 2. See if there is data held within these files in this order and update a dictionary
        #       Check for extracted audio: should be one
        #       Check for audio with silence removed: should be one or more
        #       Check for any transcriptions : should be one or more
        #       Check for any translations: should be one or more
        #       Check for any subtitle files in source_language: should be one or more
        #       Check for any subtitle files in source_language: should be one or more

        #       Any break in the chain,
        #           stop -> go find global state json, file name must not be temp.txt, if so go to next one
        #           go to speech chunks -> check none called temp, rebuild them from json, this may be achievable
        #           from global state, will just have to see


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
