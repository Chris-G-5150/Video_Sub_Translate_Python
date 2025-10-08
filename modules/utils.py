from dataclasses import asdict
from pathlib import Path
from typing import Any, Type, TypeVar

T = TypeVar("T")


class Utils:
    def __init__(self, app_base_dir) -> None:
        self.app_base_dir = app_base_dir

    def build_file_os_path(self, *parts: str | Path) -> Path:
        app_base_dir = self.app_base_dir
        returns = app_base_dir.joinpath(*parts)
        return returns

    # @staticmethod
    # def add_speech_chunk(speech_chunk: SpeechChunk):
    #     config  = self.global_confg.speech_chun.append(speech_chunk)

    @staticmethod
    def check_class_property_exists(class_self, class_property: str) -> bool:
        exists = hasattr(class_self, class_property)
        status = "exists" if exists else "does not exist"
        print(f"property: {class_property} {status} on {class_self.__class__.__name__}")
        return exists

    @staticmethod
    def dict_to_obj(data: dict, cls: Type[T]) -> T:
        """Turn a dict into a dataclass object."""
        return cls(**data)

    @staticmethod
    def obj_to_dict(obj: Any) -> dict:
        """Turn a dataclass object into a dict."""
        return asdict(obj)
