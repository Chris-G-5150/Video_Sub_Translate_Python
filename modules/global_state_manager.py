from pathlib import Path

from data_types_and_classes.data_constants import StateSteps, StateStepsReference
from data_types_and_classes.data_types import AppParams


class GlobalStateManager:
	def __init__(
		self,
		app_base_dir: Path,
		app_params: AppParams,
	):
		self.app_base_dir = (app_base_dir,)
		self.app_params = (app_params,)
		self.state_steps = StateSteps
		self.global_config = None
		self.current_state_step = None

		self.current_state_step = None

	def get_current_state_step(self, name_of_state):
		return getattr(self.state_steps, state_ref)

	def set_current_state_step(self, name_of_state):
		state_ref = StateStepsReference[name_of_state]
		self.current_state_step = getattr(self.state_steps, state_ref)

	def update_current_state_step(self, name_of_state, properties_to_update: dict):
		state_ref = StateStepsReference[name_of_state]

		target = getattr(self.current_state_step, state_ref, None)
		if not target:
			return  # or raise an error if missing

		for change, new_value in properties_to_update.items():
			if target.get(change) is None:
				target[change] = new_value

	def init(
		self,
	):
		self.current_state_ref = StateStepsReference.Start
		self.build_application_dependencies()

	def set_current_state_step(self, state_step: str):
		self.state_container.set_current_state_step = getattr(
			self.state_container.state_steps, state_step
		)

	def get_current_app_state_step(self):
		return self.state_container.current_state_step

	def build_application_dependencies(self):
		self.data_initializer = DataInitializer(
			app_params=self.app_params,
			app_base_dir=self.app_base_dir,
		)
