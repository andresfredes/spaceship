from enum import Enum as BaseEnum


class Enum(BaseEnum):
    def __repr__(self):
        return f"{self.__class__.__name__}.{self.__name__}:({self.value})"


class Colour(Enum):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
