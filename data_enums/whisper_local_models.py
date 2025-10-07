from enum import Enum


class WhisperMultiLingualModels(str, Enum):
    Tiny = "tiny"
    Base = "base"
    Small = "small"
    Medium = "medium"
    Large = "large"
    Turbo = "turbo"

    @classmethod
    def has_value(cls, value: str) -> bool:
        return value in cls._value2member_map_

    def __str__(self) -> str:
        return self.value


class WhisperEnglishModels(str, Enum):
    TinyEn = "tiny.en"
    BaseEn = "base.en"
    SmallEn = "small.en"
    MediumEn = "medium.en"

    @classmethod
    def has_value(cls, value: str) -> bool:
        return value in cls._value2member_map_

    def __str__(self) -> str:
        return self.value
