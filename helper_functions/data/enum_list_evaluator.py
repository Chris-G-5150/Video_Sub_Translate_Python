from enum import Enum


def evaluate_enum_list(value: str, enum_list: list[Enum]) -> str:
    for enum_class in enum_list:
        try:
            return enum_class[value].value  # ✅ correct
        except KeyError:
            continue
    raise ValueError(f"'{value}' not found in any registered Enums.")
