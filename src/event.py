import pygame

from src.settings import settings
from src.state import state


class EventHandler:
    def __init__(self):
        pass

    def step(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == settings.LEFT_CLICK:
                    state.hand.hold_card(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == settings.LEFT_CLICK:
                    state.hand.unhold_card()
            if event.type == pygame.MOUSEMOTION:
                state.hand.move_held_card(event.rel)
            if event.type == pygame.QUIT:
                return False
        return True
