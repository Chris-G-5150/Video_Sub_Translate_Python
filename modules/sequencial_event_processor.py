from data_enums.event_processor_enums import CompletionStatus, EventStatus


class Event:
	def __init__(self, order, event_name, requesting_class_ref, function_ref):
		self.order = order
		self.event_name = event_name
		self.parent_class_ref = requesting_class_ref
		self.function_ref = function_ref
		self.status = None
		self.completed = CompletionStatus.NOT_STARTED
		self.error_message = None

	def __repr__(self):  # noqa: N807
		return f"<Event {self.event_name} ({self.status})>"


class SequentialEventsProcessor:
	def __init__(self, class_being_processed, on_complete=None):
		self.event_list = self.class_being_processed.get_events_list()
		self.events = None
		self.current_event = None
		self.currently_running = False
		self.on_complete = on_complete

	def build_events_from_class_events_list(self):
		events = []
		for event in self.event_list:
			events.append(
				Event(
					order=event.order,
					event_name=event.event_name,
					class_ref=event.class_ref,
					function_ref=event.function_ref,
				)
			)

		return dict(sorted(events.items()))

	def run_sequence(self):
		if not self.events:
			print("[ERROR] No events to process.")
			return
		first_key = min(self.events.keys())
		self.trigger_event(self.events[first_key])

	def trigger_event(self, event):
		self.current_event = event
		self.currently_running = True
		print(f"[INFO] Running {event.event_name}...")

		try:
			fn = getattr(event.class_ref, event.function_name)
			fn()  # Run the actual method
			event.status = EventStatus.OK
			event.completed = CompletionStatus.COMPLETE
		except Exception as e:
			event.status = EventStatus.ERROR
			event.error_message = str(e)
			event.completed = CompletionStatus.COMPLETE

	def process_result(self, event):
		self.current_event = None
		self.currently_running = False

		if event.status == EventStatus.OK:
			print(f"[OK] {event.event_name} complete. Proceeding...")
			self.trigger_next_event(event)
		else:
			print(f"[ERROR] {event.event_name} failed: {event.error_message}")
			print("[INFO] Stopping sequence due to error.")

	def finish_sequence(self):
		print("[INFO] Event sequence completed successfully.")
		if self.on_complete:
			self.on_complete()
