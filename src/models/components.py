from abc import ABC, abstractmethod

from src.models.types import Position


class DrawMixin(ABC):
    @property
    @abstractmethod
    def surface(self): ...

    @property
    @abstractmethod
    def pos(self): ...

    def draw(self, surface):
        surface.blit(self.surface, self.pos)


class MouseMixin(ABC):
    _mouse_held = False

    @property
    @abstractmethod
    def bounds(self): ...

    def click_down(self, pos):
        if not self.bounds.collidepoint(pos):
            return
        self._mouse_held = True
        self.on_mouse_down(pos)

    def click_up(self, pos):
        if not self._mouse_held:
            return
        self._mouse_held = False
        self.on_mouse_up(pos)

    def hover(self, pos):
        if not self.bounds.collidepoint(pos):
            return
        self.on_hover(pos)

    def on_mouse_down(self, pos):
        pass

    def on_mouse_up(self, pos):
        pass

    def on_hover(self, pos):
        pass


class MouseMoveMixin(ABC):
    @property
    @abstractmethod
    def pos(self) -> Position: ...

    @pos.setter
    @abstractmethod
    def pos(self, val): ...

    @property
    @abstractmethod
    def bounds(self): ...

    def mouse_move(self, rel, init_override=False):
        if not self._mouse_held and not init_override:
            return
        self.pos = (self.pos[0] + rel[0], self.pos[1] + rel[1])
        self.bounds.update(
            self.pos[0], self.pos[1], self.bounds.width, self.bounds.height
        )
        self.on_move(rel)

    def on_move(self, rel):
        pass
