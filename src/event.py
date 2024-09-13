import pygame


class EventHandler:
    def __init__(self, hand):
        self.hand = hand

    def step(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.hand.hold_card(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.hand.unhold_card()
            if event.type == pygame.MOUSEMOTION:
                self.hand.move_held_card(event.rel)
            if event.type == pygame.QUIT:
                return False
        return True
