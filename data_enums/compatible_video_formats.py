from enum import Enum


class CompatibleVideoFormats(str, Enum):
    MP4 = "mp4"
    MKV = "mkv"
    WEBM = "webm"
    FLV = "flv"
    AVI = "avi"
    MOV = "mov"
    WMV = "wmv"
    M4V = "m4v"

    @classmethod
    def has_value(cls, value: str) -> bool:
        return value in cls._value2member_map_

    def __str__(self) -> str:
        return self.value
