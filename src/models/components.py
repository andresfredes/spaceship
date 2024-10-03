class BaseObject:
    _pos = None
    _surface = None
    _bounds = None
    hoverable = False
    clickable = False
    movable = False


class Container:
    _items = []

    def __iter__(self):
        for item in self._items:
            yield item


class DrawMixin:
    def __init_subclass__(self):
        if not hasattr(self, "_surface") or not hasattr(self, "_pos"):
            raise NotImplementedError("DrawMixin subclass missing attribute(s)")

    def draw(self, surface):
        surface.blit(self._surface, self._pos)


class MouseMixin:
    _mouse_held = False

    def __init_subclass__(self):
        if (
            not hasattr(self, "_bounds")
            or not hasattr(self, "_pos")
            or not hasattr(self, "hoverable")
            or not hasattr(self, "clickable")
            or not hasattr(self, "moveable")
        ):
            raise NotImplementedError("MouseMixin subclass missing attribute(s)")

    def click_down(self, pos):
        print(f"POS: {pos}, BOUNDS: {self._bounds}")
        if not self._bounds.collidepoint(pos):
            return
        self._mouse_held = True
        self.on_mouse_down(pos)

    def click_up(self, pos):
        if not self._mouse_held:
            return
        self._mouse_held = False
        self.on_mouse_up(pos)

    def mouse_move(self, rel, init_override=False):
        if not self._mouse_held and not init_override:
            return
        self._pos = (self._pos[0] + rel[0], self._pos[1] + rel[1])
        self._bounds.update(
            self._pos[0], self._pos[1], self._bounds.width, self._bounds.height
        )
        self.on_move(rel)

    def hover(self, pos):
        if not self._bounds.collidepoint(pos):
            return
        self.on_hover(pos)

    def on_mouse_down(self, pos):
        pass

    def on_mouse_up(self, pos):
        pass

    def on_move(self, rel):
        pass

    def on_hover(self, pos):
        pass
