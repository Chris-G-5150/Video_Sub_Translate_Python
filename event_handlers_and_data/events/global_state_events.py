from typing import TypeVar

from event_handlers_and_data.event_handler import EventStatus, StatusData

T = TypeVar("T")


class GlobalStateEvents:
    @staticmethod
    def DATA_INITIALIZER_INIT_COMPLETED() -> StatusData:
        return StatusData(
            status=EventStatus.OK,
            status_message="[GLOBAL STATE] Data Initializer initialization completed successfully.",
        )

    @staticmethod
    def DATA_INITIALIZER_INIT_FAILED(error: Exception | str) -> StatusData:
        return StatusData(
            status=EventStatus.ERROR,
            status_message=f"[GLOBAL STATE] Data Initializer initialization failed: {error}",
        )

    @staticmethod
    def STATE_STEP_CHANGED(new_state: str) -> StatusData:
        return StatusData(
            status=EventStatus.OK,
            status_message=f"[GLOBAL STATE] State step changed to: {new_state}",
        )
