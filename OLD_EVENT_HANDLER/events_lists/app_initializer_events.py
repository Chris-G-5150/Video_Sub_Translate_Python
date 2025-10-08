from dataclasses import dataclass
from enum import Enum
from typing import Optional
from helper_classes.extended_enum import ExtendedEnum
from event_handlers_and_data.base_event_types import EventStatus, StatusData

# from event_handlers_and_data.event_handler import EventStatus, StatusData


class AppEventListeners(ExtendedEnum):
	"""
	Enum of event names for AppEvents.
	Used to ensure consistent event naming and prevent typos.
	"""

	GLOBAL_STATE_MANAGER_INIT = "GLOBAL_STATE_MANAGER_INIT"

	@classmethod
	def as_dict(cls) -> dict[str, str]:
		"""Return a dictionary of event names and values."""
		return {member.name: member.value for member in cls}


@dataclass
class AppEvents(Enum):
	@staticmethod
	def GLOBAL_STATE_MANAGER_INIT(  # noqa: N802
		status: EventStatus, error: Optional[Exception | str] = None
	) -> StatusData:  # noqa: N802
		if status == EventStatus.OK:
			return StatusData(
				status=EventStatus.OK, status_message="[APP] GLOBAL STATE MANAGER READY."
			)
		else:
			return StatusData(
				status=EventStatus.ERROR,
				status_message=f"[APP] GLOBAL STATE MANAGER FAILED: {error}",
			)
