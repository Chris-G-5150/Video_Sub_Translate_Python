from enum import Enum, auto


class EventStatus(Enum):
    OK = auto()
    ERROR = auto()


class CompletionStatus(Enum):
    NOT_STARTED = auto()
    IN_PROGRESS = auto()
    COMPLETE = auto()


class Event:
    def __init__(self, order, event_name, class_ref, function_name):
        self.order = order
        self.event_name = event_name
        self.class_ref = class_ref
        self.function_name = function_name
        self.status = None
        self.completed = CompletionStatus.NOT_STARTED
        self.error_message = None

    def __repr__(self):
        return f"<Event {self.event_name} ({self.status})>"
