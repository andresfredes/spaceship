from enum import Enum as BaseEnum

Position = list[int, int] | tuple[int, int]


class Enum(BaseEnum):
    def __repr__(self):
        return f"{self.__class__.__name__}.{self.__name__}:({self.value})"
