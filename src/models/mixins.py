class DrawMixin:
    def __init_subclass__(self):
        if not hasattr(self, "_surface") or not hasattr(self, "_pos"):
            raise NotImplementedError("DrawMixin subclass missing attribute(s)")

    def draw(self, surface):
        surface.blit(self._surface, self._pos)


class MouseMixin:
    def __init_subclass__(self):
        if not hasattr(self, "_bounds") or not hasattr(self, "_pos"):
            raise NotImplementedError("MouseMixin subclass missing attribute(s)")

    def collidepoint(self, pos):
        return self._bounds.collidepoint(pos)

    def move(self, rel):
        self._pos = (self._pos[0] + rel[0], self._pos[1] + rel[1])
        self._bounds.update(
            self._pos[0], self._pos[1], self._bounds.width, self._bounds.height
        )
