from dataclasses import dataclass
from typing import Optional, TypeVar

from event_handlers_and_data.base_event_types import EventStatus
from event_handlers_and_data.event_handler import StatusData
from helper_classes.extended_enum import ExtendedEnum

T = TypeVar("T")


class GlobalStateEventListeners(ExtendedEnum):
	"""
	Enum of event names for GlobalStateEvents.
	"""

	DATA_INITIALIZER_INIT = "DATA_INITIALIZER_INIT"  # type: ignore
	STATE_STEP_CHANGED = "STATE_STEP_CHANGED"  # type: ignore

	@classmethod
	def as_dict(cls) -> dict[str, str]:
		"""Return a dictionary of event names and values."""
		return {member.name: member.value for member in cls}


@dataclass
class GlobalStateEvents:
	"""
	Unified Global State events.
	Each event returns a single StatusData object with either OK or ERROR status.
	"""

	@staticmethod
	def DATA_INITIALIZER_INIT(  # noqa: N802
		status: EventStatus, error: Optional[Exception | str] = None
	) -> StatusData:
		if status == EventStatus.OK:
			return StatusData(
				status=EventStatus.OK,
				status_message="[GLOBAL STATE] Data Initializer initialization completed successfully.",
			)
		return StatusData(
			status=EventStatus.ERROR,
			status_message=f"[GLOBAL STATE] Data Initializer initialization failed: {error}",
		)

	@staticmethod
	def STATE_STEP_CHANGED(new_state: str) -> StatusData:  # noqa: N802
		"""
		Emits a status update when the global state step changes.
		This always represents a successful change event.
		"""
		return StatusData(
			status=EventStatus.OK,
			status_message=f"[GLOBAL STATE] State step changed to: {new_state}",
		)
