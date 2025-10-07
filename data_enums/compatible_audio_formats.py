from enum import Enum


class CompatibleAudioFormats(str, Enum):
    WAV = "wav"
    OGG = "ogg"
    MP3 = "mp3"

    @classmethod
    def has_value(cls, value: str) -> bool:
        return value in cls._value2member_map_

    def __str__(self) -> str:
        return self.value
