from dataclasses import dataclass

from event_handlers_and_data.event_handler import EventStatus, StatusData


@dataclass
class FileManagerEvents:
    @staticmethod
    def FILE_EXISTS(filepath: str) -> StatusData:
        return StatusData(
            status=EventStatus.OK,
            status_message=f"[FILE MANAGER] File exists: {filepath}",
        )

    @staticmethod
    def FILE_DOES_NOT_EXIST(filepath: str) -> StatusData:
        return StatusData(
            status=EventStatus.ERROR,
            status_message=f"[FILE MANAGER] File does not exist: {filepath}",
        )

    @staticmethod
    def DIRECTORY_EXISTS(directory: str) -> StatusData:
        return StatusData(
            status=EventStatus.OK,
            status_message=f"[FILE MANAGER] Directory exists: {directory}",
        )

    @staticmethod
    def DIRECTORY_DOES_NOT_EXIST(directory: str) -> StatusData:
        return StatusData(
            status=EventStatus.ERROR,
            status_message=f"[FILE MANAGER] Directory does not exist: {directory}",
        )

    @staticmethod
    def DIRECTORY_BUILT_IN_FILE_SYSTEM_OK(directory: str) -> StatusData:
        return StatusData(
            status=EventStatus.OK,
            status_message=f"[FILE MANAGER] Directory successfully built in file system: {directory}",
        )

    @staticmethod
    def DIRECTORY_BUILT_IN_FILE_SYSTEM_ERROR(
        directory: str, error: Exception | str
    ) -> StatusData:
        return StatusData(
            status=EventStatus.ERROR,
            status_message=f"[FILE MANAGER] Failed to build directory in file system: {directory} | Error: {error}",
        )

    @staticmethod
    def ALL_DIRECTORIES_BUILT_OKAY(directories: list[str]) -> StatusData:
        return StatusData(
            status=EventStatus.OK,
            status_message=f"[FILE MANAGER] All directories built successfully: {', '.join(directories)}",
        )

    @staticmethod
    def ALL_DIRECTORIES_BUILT_ERROR(
        directories: list[str], error: Exception | str
    ) -> StatusData:
        return StatusData(
            status=EventStatus.ERROR,
            status_message=f"[FILE MANAGER] Error while building directories ({', '.join(directories)}): {error}",
        )

    @staticmethod
    def TRANSCRIPTION_FILE_PATH_CREATED_OKAY(filepath: str) -> StatusData:
        return StatusData(
            status=EventStatus.OK,
            status_message=f"[FILE MANAGER] Transcription file path created successfully: {filepath}",
        )

    @staticmethod
    def TRANSCRIPTION_FILE_PATH_CREATED_ERROR(
        filepath: str, error: Exception | str
    ) -> StatusData:
        return StatusData(
            status=EventStatus.ERROR,
            status_message=f"[FILE MANAGER] Failed to create transcription file path ({filepath}): {error}",
        )

    @staticmethod
    def FILE_WRITTEN_TO_DISK_OKAY(filepath: str) -> StatusData:
        return StatusData(
            status=EventStatus.OK,
            status_message=f"[FILE MANAGER] File written to disk successfully: {filepath}",
        )

    @staticmethod
    def FILE_WRITTEN_TO_DISK_ERROR(filepath: str, error: Exception | str) -> StatusData:
        return StatusData(
            status=EventStatus.ERROR,
            status_message=f"[FILE MANAGER] Failed to write file to disk ({filepath}): {error}",
        )

    @staticmethod
    def STATE_JSON_WRITTEN_TO_DISK_OKAY(speech_chunk_filepath: str) -> StatusData:
        return StatusData(
            status=EventStatus.OK,
            status_message=f"[FILE MANAGER] State JSON written to disk successfully: {speech_chunk_filepath}",
        )

    @staticmethod
    def STATE_JSON_WRITTEN_TO_DISK_ERROR(
        speech_chunk_filepath: str, error: Exception | str
    ) -> StatusData:
        return StatusData(
            status=EventStatus.ERROR,
            status_message=f"[FILE MANAGER] Failed to write state JSON to disk ({speech_chunk_filepath}): {error}",
        )
