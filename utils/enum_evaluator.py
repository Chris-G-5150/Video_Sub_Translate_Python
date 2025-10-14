from enum import Enum
from typing import TypeVar

T = TypeVar("T", bound=Enum)


def evaluate_enum(value: str | T | None, enum_class: type[T]) -> str:
	if value is None:
		raise ValueError(f"Cannot evaluate None for {enum_class.__name__}")

	if isinstance(value, enum_class):
		return value.value

	if isinstance(value, str) and value in enum_class._value2member_map_:
		return value

	raise ValueError(f"{value!r} is not a valid member of {enum_class.__name__}")
