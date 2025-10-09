from collections.abc import Iterable


class ClassEventListItem:
	def __init__(
		self, order: int, event_name: str, function_ref, class_ref: Iterable[object] | None = None
	):
		self.order = (order,)
		self.event_name = event_name
		self.class_ref = class_ref
		self.function_ref = function_ref


# This will be for a much bgger machine which can offload a bunch of manual calls,
# the events themselves will be held within the classes with a classname.get_events_list() call like in data initialization
class AutomationProcessorListItem:
	def __init__(self, order: int, automated_class: type[any], automated_class_params):
		self.automated_class = (automated_class,)
		self.automated_class_params = automated_class_params
