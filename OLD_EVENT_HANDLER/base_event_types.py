from dataclasses import dataclass
from enum import Enum


class EventStatus(Enum):
    OK = "OK"
    ERROR = "ERROR"


@dataclass
class StatusData:
    status: str | EventStatus
    status_message: str = ""
