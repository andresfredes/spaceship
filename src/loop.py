import pygame

from src.event import EventHandler
from src.render import Renderer


class GameLoop:
    def __init__(self):
        self.running = True

    def __enter__(self):
        pygame.init()
        self._renderer = Renderer()
        self._event_handler = EventHandler()
        return self

    def __exit__(self, exc_type=None, exc_val=None, tb=None):
        if exc_type:
            print(exc_val, tb)
        pygame.quit()

    def run(self):
        while self.running:
            self.running = self._event_handler.step()
            self._renderer.render_frame()
