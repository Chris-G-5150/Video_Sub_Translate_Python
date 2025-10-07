from pathlib import Path
from typing import Optional, Union

from data_classes.global_config import DataInitializationStatus, GlobalConfig
from data_classes.global_state import ClassInitializationStatus
from data_classes.state_steps import StateStep, state_steps
from event_handlers_and_data.event_dispatchers import EventDispatchers
from event_handlers_and_data.events.global_state_events import GlobalStateEvents
from module_parameters.app_params import AppParams
from modules.console_animator import ConsoleAnimator
from modules.data_initializer import DataInitializer
from modules.utils import Utils


class GlobalStateManager:
    def __init__(
        self,
        app_base_dir: Path,
        app_params: AppParams,
        utils: Utils,
        console_animator: ConsoleAnimator | None = None,
        global_config: Optional[GlobalConfig] = None,
        global_state_dispatcher: EventDispatchers | None = None,
    ):
        self.app_base_dir = app_base_dir
        self.app_params = app_params
        self.console_animator = console_animator
        self.utils = utils
        self.state_steps = state_steps
        self.current_state_step = None
        self.class_initialization_status = ClassInitializationStatus()
        self.data_initialization_status = DataInitializationStatus()
        self.data_initializer = DataInitializer(
            app_params=app_params,
            utils=utils,
            console_animator=console_animator,
            app_base_dir=app_base_dir,
        )
        self.console_animator = console_animator
        self.global_config = global_config
        self.global_state_dispatcher = EventDispatchers.global_state_dispatcher
        self.add_listener = self.global_state_dispatcher.add_listener
        self.trigger_event = self.global_state_dispatcher.trigger_event
        self.init_event_listeners()

    def init_event_listeners(self):
        self.add_listener(self.on_data_initializer_init_complete)
        self.add_listener(self.state_manager.ondata_initializer_init_failed)
        self.add_listener(self.on_state_step_changed)

    def on_data_intializer_init_complete(self, StatusData):
        print(StatusData.status_message)
        self.trigger_event(GlobalStateEvents.DATA_INITIALIZER_INIT_COMPLETED)

    def on_data_initializer_init_failed(self, StatusData):
        print(StatusData.status_message)
        self.trigger_event(GlobalStateEvents.STATE_STEP_CHANGED)

    def state_step_changed(self, StatusData):
        print(StatusData.status_message)
        self.trigger_event(GlobalStateEvents.DATA_INITIALIZER_INIT_COMPLETED)

    def set_current_state_step(self, state_step: StateStep):
        self.current_state_step = state_step

    def get_current_app_state_step(self):
        return self.current_state_step

    def init_data_initializer(self):
        self.data_initializer = DataInitializer(
            app_params=self.app_params,
            app_base_dir=self.app_base_dir,
            utils=self.utils,
            console_animator=self.console_animator,
        )
        self.global_state_dispatcher.trigger_event(
            GlobalStateEvents.DATA_INITIALIZER_INIT_COMPLETED
        )

    def get_full_global_app_state(
        self,
    ) -> dict[
        str, Union[StateStep, ClassInitializationStatus, DataInitializationStatus]
    ]:
        return {
            "current_state_step": self.current_state_step,
            "class_init_status": self.class_initialization_status,
            "data_init_status": self.data_initialization_status,
        }

    #
    # def state_step_check(self):
    #     directories = this.directories
    #     state_json_file_path.read_text(encoding="utf-8")
    #     app_base_dir_exists = file_manager.check_directroy_exists(directories.app_base_dir)
    #     json_dir_exists = file_manager.check_directroy_exists(directories.speech_chunk_json_dir)
    #     extracted_audio_dir_exists = file_manager.check_directroy_exists(directories.app_base_dir)
    #     if app_base_dir_exists and not json_dir_exists:
    #         # check the states and test
    #         'd'
    #         if json_dir_exists
