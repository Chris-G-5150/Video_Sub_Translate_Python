from dataclasses import dataclass
from enum import Enum

from event_handlers_and_data.event_handler import EventStatus, StatusData


@dataclass
class DataInitializerEvents(Enum):
    @staticmethod
    def GLOBAL_CONFIG_COMPLETED() -> StatusData:
        return StatusData(
            status=EventStatus.OK,
            status_message="[DATA INITIALIZER] Global configuration completed successfully.",
        )

    @staticmethod
    def GLOBAL_CONFIG_FAILED(error: Exception | str) -> StatusData:
        return StatusData(
            status=EventStatus.ERROR,
            status_message=f"[DATA INITIALIZER] Global configuration failed: {error}",
        )

    @staticmethod
    def APP_PATHS_TO_FILES_COMPLETED() -> StatusData:
        return StatusData(
            status=EventStatus.OK,
            status_message="[DATA INITIALIZER] Application paths to files initialized successfully.",
        )

    @staticmethod
    def APP_PATHS_TO_FILES_FAILED(error: Exception | str) -> StatusData:
        return StatusData(
            status=EventStatus.ERROR,
            status_message=f"[DATA INITIALIZER] Application paths to files initialization failed: {error}",
        )

    @staticmethod
    def APP_DIRECTORIES_COMPLETED() -> StatusData:
        return StatusData(
            status=EventStatus.OK,
            status_message="[DATA INITIALIZER] Application directories setup completed successfully.",
        )

    @staticmethod
    def APP_DIRECTORIES_FAILED(error: Exception | str) -> StatusData:
        return StatusData(
            status=EventStatus.ERROR,
            status_message=f"[DATA INITIALIZER] Application directories setup failed: {error}",
        )

    @staticmethod
    def MEDIA_DATA_COMPLETED() -> StatusData:
        return StatusData(
            status=EventStatus.OK,
            status_message="[DATA INITIALIZER] Media data setup completed successfully.",
        )

    @staticmethod
    def MEDIA_DATA_FAILED(error: Exception | str) -> StatusData:
        return StatusData(
            status=EventStatus.ERROR,
            status_message=f"[DATA INITIALIZER] Media data setup failed: {error}",
        )

    @staticmethod
    def AUDIO_EXTRACTION_CONFIG_COMPLETED() -> StatusData:
        return StatusData(
            status=EventStatus.OK,
            status_message="[DATA INITIALIZER] Audio extraction configuration completed successfully.",
        )

    @staticmethod
    def AUDIO_EXTRACTION_CONFIG_FAILED(error: Exception | str) -> StatusData:
        return StatusData(
            status=EventStatus.ERROR,
            status_message=f"[DATA INITIALIZER] Audio extraction configuration failed: {error}",
        )

    @staticmethod
    def BASE_FILE_NAMES_COMPLETED() -> StatusData:
        return StatusData(
            status=EventStatus.OK,
            status_message="[DATA INITIALIZER] Base file names setup completed successfully.",
        )

    @staticmethod
    def BASE_FILE_NAMES_FAILED(error: Exception | str) -> StatusData:
        return StatusData(
            status=EventStatus.ERROR,
            status_message=f"[DATA INITIALIZER] Base file names setup failed: {error}",
        )
