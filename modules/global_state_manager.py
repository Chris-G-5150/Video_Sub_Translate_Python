from pathlib import Path
from typing import Optional

from data_classes import state_steps
from data_classes.global_config import GlobalConfig
from data_classes.state_steps import StateSteps
from module_parameters.app_params import AppParams
from modules.console_animator import ConsoleAnimator
from modules.data_initializer import DataInitializer
from modules.utils import Utils

State


class GlobalStateManager:
    def __init__(
        self,
        app_base_dir: Path,
        app_params: AppParams,
        utils: Utils,
        console_animator: ConsoleAnimator | None = None,
        global_config: Optional[GlobalConfig] = None,
    ):
        self.app_base_dir = app_base_dir
        self.app_params = app_params
        self.console_animator = console_animator
        self.utils = utils
        self.state_steps = state_steps
        self.current_state_step = None
        self.data_initializer = None
        self.console_animator = console_animator
        self.global_config = global_config
        self.sequential_startup_machine = SequntialEventProcessor()

    def set_current_state_step(self, state_step: StateSteps):
        self.current_state_step = state_step

    def get_current_app_state_step(self):
        return self.current_state_step

    def automate_startup(self):

    def init_data_initializer(self):
        self.data_initializer = DataInitializer(
            app_params=self.app_params,
            app_base_dir=self.app_base_dir,
            utils=self.utils,
            console_animator=self.console_animator,
        )
