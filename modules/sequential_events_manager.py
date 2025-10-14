import sys
from collections.abc import Callable
from pathlib import Path
from typing import Any

# Go up 4 levels from this file → project root
ROOT = Path(__file__).resolve().parents[4]
if str(ROOT) not in sys.path:
	sys.path.insert(0, str(ROOT))


class SequentialEventsManager:
	def __init__(
		self,
		class_event_list: list[ClassEventListItem] | None = None,
		on_complete=Callable[..., Any] | None,
	):
		self.class_event_list = class_event_list
		self.events = None
		self.current_event = None
		self.currently_running = False
		self.on_complete = on_complete

	def set_events_list(self, new_events_list: list[ClassEventListItem]):
		self.class_event_list = new_events_list
		event_names = []
		for event in self.class_event_list:
			event_names.append(event.event_name)

		escape_added_events = "\n".join(event_names)

		print(f"[SEP] - New Events List Applied - {escape_added_events}")

	def build_events_from_class_events_list(self):
		if not self.class_event_list:
			return

		events = [
			Event(
				order=e.order,
				event_name=e.event_name,
				class_ref=e.class_ref,
				function_ref=e.function_ref,
			)
			for e in self.class_event_list
		]

		events.sort(key=lambda e: e.order)
		self.events = {e.order: e for e in events}
		self.run_sequence()

	def run_sequence(self):
		if not self.events:
			print("[ERROR] No events to process.")
			return
		first_key = min(self.events.keys())
		self.trigger_event(self.events[first_key])

	def trigger_event(self, event: Event):
		self.current_event = event
		self.currently_running = True
		print(f"[INFO] Running {event.event_name}...")

		try:
			self.current_event.function_ref()  # Run the actual method
			event.status = EventStatus.OK  # type: ignore
			event.completed = CompletionStatus.COMPLETE
			self.process_result(self.current_event)
		except Exception as e:
			event.status = EventStatus.ERROR  # type: ignore
			event.error_message = str(e)  # type: ignore
			event.completed = CompletionStatus.COMPLETE

	def process_result(self, event: Event):
		if self.currently_running:
			self.currently_running = False

		if event.status == EventStatus.OK:
			print(f"[OK] {event.event_name} complete. Proceeding...")
			current_event_in_sequence = self.current_event.order  # type: ignore
			next_event_order = current_event_in_sequence + 1
			print(f"nexty event order = {next_event_order}")

			for next_event in self.events:
				if next_event.order == next_event_order:
					self.current_event = None
					self.trigger_event(next_event)

				else:
					self.finish_sequence()

		else:
			print(f"[ERROR] {event.event_name} failed: {event.error_message}")
			print("[INFO] Stopping sequence due to error.")

	def finish_sequence(self):
		print("[INFO] Event sequence completed successfully.")
		if self.on_complete:
			self.on_complete()  # type: ignore


	def build_global_config_events(self, data_initializer: DataInitializer):
		return [
			ClassEventListItem(
				order=1,
				event_name="global_config_media_data",
				class_ref=data_initializer,
				function_ref=data_initializer.init_media_data,
			),
			ClassEventListItem(
				order=2,
				event_name="global_config_audio_extraction_config",
				class_ref=data_initializer,
				function_ref=data_initializer.init_audio_extraction_config,
			),
			ClassEventListItem(
				order=3,
				event_name="global_config_app_directories",
				class_ref=data_initializer,
				function_ref=data_initializer.init_app_directories,
			),
			ClassEventListItem(
				order=4,
				event_name="global_config_base_file_names",
				class_ref=data_initializer,
				function_ref=data_initializer.init_app_directories,
			),
			ClassEventListItem(
				order=5,
				event_name="global_config_app_paths_to_files",
				class_ref=data_initializer,
				function_ref=data_initializer.init_app_paths_to_files,
			),
			ClassEventListItem(
				order=6,
				event_name="global_config_create_global_config",
				class_ref=data_initializer,
				function_ref=data_initializer.build_global_config,
			),
		]
