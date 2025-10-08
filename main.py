from pathlib import Path

from data_enums.compatible_audio_formats import CompatibleAudioFormats
from data_enums.compatible_video_formats import CompatibleVideoFormats
from data_enums.iso_639_languages import ISO639Language
from data_enums.iso_3166_regions import ISO3166Regions
from data_enums.whisper_local_models import WhisperEnglishModels
from debug_tools.debug_printer import printer
from event_handlers_and_data.base_event_types import EventStatus, StatusData
from event_handlers_and_data.event_decorator import emits
from event_handlers_and_data.event_dispatchers import EventDispatchers
from module_parameters.app_params import AppParams
from modules.console_animator import ConsoleAnimator
from modules.global_state_manager import GlobalStateManager
from modules.utils import Utils

BASE_DIRECTORY = Path(__file__).resolve().parent


# GLOBAL DEBUGGER DISABLED IF ENV NOT SET CORRECTLY###################################
# not included in git repo nor is the debugger itself
# GLOBAL DEBUGGER DISABLED IF ENV NOT SET CORRECTLY###################################


class App:
    def __init__(
        self,
        app_params: AppParams,
        # noqa: E251 # type: ignore
    ):
        from event_handlers_and_data.events_lists.app_initializer_events import AppEventListeners

        self.event_list_registry = AppEventListeners.as_dict()
        # Classes that take care of each part of the project
        self.app_params = app_params
        self.console_animator = ConsoleAnimator()
        self.app_base_directory = BASE_DIRECTORY
        self.project_title = self.app_params.project_title
        self.utils = Utils(BASE_DIRECTORY)
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
        self.events_dispatcher = EventDispatchers.app_dispatcher
        self.add_listener = self.events_dispatcher.add_listener
        self.trigger_event = self.events_dispatcher.trigger_event

    def init_event_listeners(self) -> None:  # type: ignore
        print(self.event_list_registry)
        printer(
            self.events_dispatcher.add_listener(
                self.event_list_registry["GLOBAL_STATE_MANAGER_INIT"],
                self.on_global_state_manager_init,
            )
        )

    def init(self):
        self.init_event_listeners()
        self.build_global_state_manager()

    @emits()
    def build_global_state_manager(self):
        self.global_state_manager = GlobalStateManager(
            app_base_dir=BASE_DIRECTORY,
            app_params=self.app_params,
            utils=self.utils,
            global_config=None,
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
