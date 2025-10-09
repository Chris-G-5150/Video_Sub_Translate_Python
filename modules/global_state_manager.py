from pathlib import Path

from data_classes.state_steps import StateSteps, StateStepsReference
from module_parameters.app_params import AppParams
from modules.console_animator import ConsoleAnimator


class GlobalStateManager:
	def __init__(
		self,
		app_base_dir: Path,
		app_params: AppParams,
		console_animator: ConsoleAnimator | None = None,
		global_config: GlobalConfig | None = None,
	):
		self.app_base_dir = app_base_dir
		self.app_params = app_params
		self.console_animator = console_animator
		self.state_container = StateSteps()
		self.data_initializer = None
		self.global_config = global_config
		self.automation_manager = AutomationManager

	def init(self):
		self.state_container.set_current_state_step(StateStepsReference.Start)
		self.build_application_dependencies()

	def set_current_state_step(self, state_step: StateStepsReference):
		self.state_container.set_current_state_step = getattr(
			self.state_container.state_steps, state_step
		)

	def get_current_app_state_step(self):
		return self.state_container.current_state_step

	def build_application_dependencies(self):
		self.data_initializer = DataInitializer(
			app_params=self.app_params,
			app_base_dir=self.app_base_dir,
			utils=self.utils,
			console_animator=self.console_animator,
		)
