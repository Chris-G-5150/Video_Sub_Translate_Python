from dataclasses import dataclass
from enum import Enum
from typing import Callable, List


@dataclass
class EventStatus(Enum):
    OK = None
    ERROR = "ERROR"


@dataclass
class StatusData:
    status: str | EventStatus
    status_message: str = ""


@dataclass
class TriggerEvent:
    action: str


class EventHandler:
    def __init__(self):
        self.listeners: List[Callable[[StatusData], None]] = []

    def add_listener(self, listener: Callable[[StatusData], None]):
        self.listeners.append(listener)

    def trigger_event(self, event_data: StatusData):
        for listener in self.listeners:
            try:
                listener(event_data)
            except Exception as e:
                print(f"[EventHandler] Listener {listener.__name__} failed: {e}")



