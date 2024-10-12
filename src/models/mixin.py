from abc import ABC, abstractmethod

from pygame.rect import Rect
from pygame.surface import Surface

from src.type import Position


class DrawMixin(ABC):
    @property
    @abstractmethod
    def surface(self) -> Surface: ...

    @property
    @abstractmethod
    def pos(self) -> Position: ...

    def draw(self, surface: Surface):
        surface.blit(self.surface, self.pos)


class MouseMixin(ABC):
    _mouse_held = False

    @property
    @abstractmethod
    def bounds(self) -> Rect: ...

    def click_down(self, pos: Position) -> None:
        if not self.bounds.collidepoint(pos):
            return
        print("click_down")
        self._mouse_held = True
        self.on_mouse_down(pos)

    def click_up(self, pos: Position) -> None:
        if not self._mouse_held:
            return
        print("click_up")
        self._mouse_held = False
        self.on_mouse_up(pos)

    def hover(self, pos: Position) -> None:
        if not self.bounds.collidepoint(pos):
            return
        print(f"hovering... ({self})")
        self.on_hover(pos)

    def on_mouse_down(self, pos: Position) -> None:
        pass

    def on_mouse_up(self, pos: Position) -> None:
        pass

    def on_hover(self, pos: Position) -> None:
        pass


class MouseMoveMixin(ABC):
    @property
    @abstractmethod
    def pos(self) -> Position: ...

    @pos.setter
    @abstractmethod
    def pos(self, val: Position) -> None: ...

    @property
    @abstractmethod
    def bounds(self) -> Rect: ...

    def mouse_move(self, rel: Position, init_override: bool = False):
        if not self._mouse_held and not init_override:
            return
        self.pos = (self.pos[0] + rel[0], self.pos[1] + rel[1])
        self.bounds.update(
            self.pos[0], self.pos[1], self.bounds.width, self.bounds.height
        )
        self.on_move(rel)

    def on_move(self, rel: Position):
        pass
