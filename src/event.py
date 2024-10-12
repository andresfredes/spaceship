from pygame import MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION, QUIT
from pygame.event import Event
from pygame.event import get as get_events

from src.enums import Enum
from src.models.mixin import MouseMixin, MouseMoveMixin
from src.state import state


class EventType(Enum):
    QUIT = QUIT
    MOUSEBUTTONDOWN = MOUSEBUTTONDOWN
    MOUSEBUTTONUP = MOUSEBUTTONUP
    MOUSEMOTION = MOUSEMOTION


class MouseButton(Enum):
    LEFT = 1
    RIGHT = 2


class EventHandler:
    def step(self):
        for event in get_events():
            match event.type:
                case EventType.QUIT.value:
                    return False
                case EventType.MOUSEBUTTONDOWN.value:
                    self.click_down(event)
                case EventType.MOUSEBUTTONUP.value:
                    self.click_up(event)
                case EventType.MOUSEMOTION.value:
                    self.motion(event)
                case _:
                    continue
        return True

    def click_down(self, event: Event):
        match event.button:
            case MouseButton.LEFT.value:
                for item in state.get_current_iter():
                    if not isinstance(item, MouseMixin):
                        continue
                    item.click_down(event.pos)

    def click_up(self, event: Event):
        match event.button:
            case MouseButton.LEFT.value:
                for item in state.get_current_iter():
                    if not isinstance(item, MouseMixin):
                        continue
                    item.click_up(event.pos)

    def motion(self, event: Event):
        for item in state.get_current_iter():
            if isinstance(item, MouseMixin):
                item.hover(event.pos)
                if isinstance(item, MouseMoveMixin):
                    item.mouse_move(event.rel)
