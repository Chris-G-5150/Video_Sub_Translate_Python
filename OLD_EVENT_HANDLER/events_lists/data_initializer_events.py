from dataclasses import dataclass
from enum import Enum
from typing import Optional

from event_handlers_and_data.base_event_types import EventStatus, StatusData

from helper_classes.extended_enum import ExtendedEnum


class DataInitializerEventListeners(ExtendedEnum):
	"""
	Enum of event names for DataInitializerEvents.
	"""

	GLOBAL_CONFIG = "GLOBAL_CONFIG"
	APP_PATHS_TO_FILES = "APP_PATHS_TO_FILES"
	APP_DIRECTORIES = "APP_DIRECTORIES"
	MEDIA_DATA = "MEDIA_DATA"
	AUDIO_EXTRACTION_CONFIG = "AUDIO_EXTRACTION_CONFIG"
	BASE_FILE_NAMES = "BASE_FILE_NAMES"

	@classmethod
	def as_dict(cls) -> dict[str, str]:
		"""Return a dictionary of event names and values."""
		return {member.name: member.value for member in cls}


@dataclass
class DataInitializerEvents(Enum):
	"""
	Unified Data Initializer events.
	Each event returns a single StatusData object with either OK or ERROR status.
	"""

	@staticmethod
	def GLOBAL_CONFIG(status: EventStatus, error: Optional[Exception | str] = None) -> StatusData:  # noqa: N802
		if status == EventStatus.OK:
			return StatusData(
				status=EventStatus.OK,
				status_message="[DATA INITIALIZER] Global configuration completed successfully.",
			)
		return StatusData(
			status=EventStatus.ERROR,
			status_message=f"[DATA INITIALIZER] Global configuration failed: {error}",
		)

	@staticmethod
	def APP_PATHS_TO_FILES(  # noqa: N802
		status: EventStatus, error: Optional[Exception | str] = None
	) -> StatusData:
		if status == EventStatus.OK:
			return StatusData(
				status=EventStatus.OK,
				status_message="[DATA INITIALIZER] Application paths to files initialized successfully.",
			)
		return StatusData(
			status=EventStatus.ERROR,
			status_message=f"[DATA INITIALIZER] Application paths to files initialization failed: {error}",
		)

	@staticmethod
	def APP_DIRECTORIES(status: EventStatus, error: Optional[Exception | str] = None) -> StatusData:  # noqa: N802
		if status == EventStatus.OK:
			return StatusData(
				status=EventStatus.OK,
				status_message="[DATA INITIALIZER] Application directories setup completed successfully.",
			)
		return StatusData(
			status=EventStatus.ERROR,
			status_message=f"[DATA INITIALIZER] Application directories setup failed: {error}",
		)

	@staticmethod
	def MEDIA_DATA(status: EventStatus, error: Optional[Exception | str] = None) -> StatusData:  # noqa: N802
		if status == EventStatus.OK:
			return StatusData(
				status=EventStatus.OK,
				status_message="[DATA INITIALIZER] Media data setup completed successfully.",
			)
		return StatusData(
			status=EventStatus.ERROR,
			status_message=f"[DATA INITIALIZER] Media data setup failed: {error}",
		)

	@staticmethod
	def AUDIO_EXTRACTION_CONFIG(  # noqa: N802
		status: EventStatus, error: Optional[Exception | str] = None
	) -> StatusData:
		if status == EventStatus.OK:
			return StatusData(
				status=EventStatus.OK,
				status_message="[DATA INITIALIZER] Audio extraction configuration completed successfully.",
			)
		return StatusData(
			status=EventStatus.ERROR,
			status_message=f"[DATA INITIALIZER] Audio extraction configuration failed: {error}",
		)

	@staticmethod
	def BASE_FILE_NAMES(status: EventStatus, error: Optional[Exception | str] = None) -> StatusData:  # noqa: N802
		if status == EventStatus.OK:
			return StatusData(
				status=EventStatus.OK,
				status_message="[DATA INITIALIZER] Base file names setup completed successfully.",
			)
		return StatusData(
			status=EventStatus.ERROR,
			status_message=f"[DATA INITIALIZER] Base file names setup failed: {error}",
		)
