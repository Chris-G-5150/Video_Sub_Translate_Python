from dataclasses import dataclass
from typing import Optional

from event_handlers_and_data.base_event_types import EventStatus, StatusData

from helper_classes.extended_enum import ExtendedEnum


class FileManagerEventListeners(ExtendedEnum):
	"""
	Enum of event names for FileManagerEvents.
	"""

	FILE_EXISTS = "FILE_EXISTS"  # type: ignore
	DIRECTORY_EXISTS = "DIRECTORY_EXISTS"  # type: ignore
	DIRECTORY_BUILT_IN_FILE_SYSTEM = "DIRECTORY_BUILT_IN_FILE_SYSTEM"  # type: ignore
	ALL_DIRECTORIES_BUILT = "ALL_DIRECTORIES_BUILT"  # type: ignore
	TRANSCRIPTION_FILE_PATH_CREATED = "TRANSCRIPTION_FILE_PATH_CREATED"  # type: ignore
	FILE_WRITTEN_TO_DISK = "FILE_WRITTEN_TO_DISK"  # type: ignore
	STATE_JSON_WRITTEN_TO_DISK = "STATE_JSON_WRITTEN_TO_DISK"  # type: ignore

	@classmethod
	def as_dict(cls) -> dict[str, str]:
		"""Return a dictionary of event names and values."""
		return {member.name: member.value for member in cls}


@dataclass
class FileManagerEvents:
	"""
	Unified File Manager events.
	Each event returns a single StatusData object with either OK or ERROR status.
	"""

	@staticmethod
	def FILE_EXISTS(  # noqa: N802
		status: EventStatus, filepath: str, error: Optional[Exception | str] = None
	) -> StatusData:
		if status == EventStatus.OK:
			return StatusData(
				status=EventStatus.OK, status_message=f"[FILE MANAGER] File exists: {filepath}"
			)
		return StatusData(
			status=EventStatus.ERROR,
			status_message=f"[FILE MANAGER] File does not exist: {filepath} | Error: {error}",
		)

	@staticmethod
	def DIRECTORY_EXISTS(  # noqa: N802
		status: EventStatus, directory: str, error: Optional[Exception | str] = None
	) -> StatusData:
		if status == EventStatus.OK:
			return StatusData(
				status=EventStatus.OK,
				status_message=f"[FILE MANAGER] Directory exists: {directory}",
			)
		return StatusData(
			status=EventStatus.ERROR,
			status_message=f"[FILE MANAGER] Directory does not exist: {directory} | Error: {error}",
		)

	@staticmethod
	def DIRECTORY_BUILT_IN_FILE_SYSTEM(  # noqa: N802
		status: EventStatus, directory: str, error: Optional[Exception | str] = None
	) -> StatusData:
		if status == EventStatus.OK:
			return StatusData(
				status=EventStatus.OK,
				status_message=f"[FILE MANAGER] Directory successfully built in file system: {directory}",
			)
		return StatusData(
			status=EventStatus.ERROR,
			status_message=f"[FILE MANAGER] Failed to build directory in file system: {directory} | Error: {error}",
		)

	@staticmethod
	def ALL_DIRECTORIES_BUILT(  # noqa: N802
		status: EventStatus, directories: list[str], error: Optional[Exception | str] = None
	) -> StatusData:
		if status == EventStatus.OK:
			return StatusData(
				status=EventStatus.OK,
				status_message=f"[FILE MANAGER] All directories built successfully: {', '.join(directories)}",
			)
		return StatusData(
			status=EventStatus.ERROR,
			status_message=f"[FILE MANAGER] Error while building directories ({', '.join(directories)}): {error}",
		)

	@staticmethod
	def TRANSCRIPTION_FILE_PATH_CREATED(  # noqa: N802
		status: EventStatus, filepath: str, error: Optional[Exception | str] = None
	) -> StatusData:
		if status == EventStatus.OK:
			return StatusData(
				status=EventStatus.OK,
				status_message=f"[FILE MANAGER] Transcription file path created successfully: {filepath}",
			)
		return StatusData(
			status=EventStatus.ERROR,
			status_message=f"[FILE MANAGER] Failed to create transcription file path ({filepath}): {error}",
		)

	@staticmethod
	def FILE_WRITTEN_TO_DISK(  # noqa: N802
		status: EventStatus, filepath: str, error: Optional[Exception | str] = None
	) -> StatusData:
		if status == EventStatus.OK:
			return StatusData(
				status=EventStatus.OK,
				status_message=f"[FILE MANAGER] File written to disk successfully: {filepath}",
			)
		return StatusData(
			status=EventStatus.ERROR,
			status_message=f"[FILE MANAGER] Failed to write file to disk ({filepath}): {error}",
		)

	@staticmethod
	def STATE_JSON_WRITTEN_TO_DISK(  # noqa: N802
		status: EventStatus, speech_chunk_filepath: str, error: Optional[Exception | str] = None
	) -> StatusData:
		if status == EventStatus.OK:
			return StatusData(
				status=EventStatus.OK,
				status_message=f"[FILE MANAGER] State JSON written to disk successfully: {speech_chunk_filepath}",
			)
		return StatusData(
			status=EventStatus.ERROR,
			status_message=f"[FILE MANAGER] Failed to write state JSON to disk ({speech_chunk_filepath}): {error}",
		)
