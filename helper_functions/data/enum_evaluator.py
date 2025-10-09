from enum import Enum
from typing import TypeVar

T = TypeVar("T", bound=Enum)


# Was getting errors so needed an enum evaluator since not familiaer with Python and the interpreter kept erroring out
def evaluate_enum(value: str | T, enum_class: type[T]) -> str:
	# Case 1: already an enum member
	if isinstance(value, enum_class):
		return value.value

	# Case 2: raw string, check validity
	if isinstance(value, str) and value in enum_class._value2member_map_:
		return value

	# Case 3: invalid
	raise ValueError(f"{value!r} is not a valid member of {enum_class.__name__}")
