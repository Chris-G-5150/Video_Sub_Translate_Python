# apply this to the enums which gives you caccess to a wonderful array, instead of calling Enum call extended Enum

from enum import Enum


class ExtendedEnum(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))
