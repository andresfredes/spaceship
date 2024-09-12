import pygame

from src.colours import Colour


class Deck:
    def __init__(self):
        self._cards = []


class Discard:
    def __init__(self):
        self._cards = []


class Hand:
    def __init__(self, cards=[]):
        self.cards = cards
        self.held_card_index = None

    def __iter__(self):
        for card in self.cards:
            yield card

    def hold_card(self, pos):
        for i, card in enumerate(self.cards):
            if card.collidepoint(pos):
                card.mouse_held = True
                self.held_card_index = i

    def unhold_card(self):
        if self.held_card_index is None:
            return
        self.cards[self.held_card_index].mouse_held = False
        self.held_card_index = None

    def move_held_card(self, rel):
        if self.held_card_index is None:
            return
        self.cards[self.held_card_index].move(rel)

    def draw(self, surface):
        for card in self.cards:
            card.draw(surface)


class Card:
    def __init__(self, pos=[50, 50]):
        self.mouse_held = False
        self._pos = pos
        # flipped
        # visible
        self._bounds = pygame.Rect(self._pos[0], self._pos[1], 50, 50)
        self._colour = Colour.WHITE.value

    def collidepoint(self, pos):
        return self._bounds.collidepoint(pos)

    def move(self, rel):
        self._bounds.update(
            self._bounds.left + rel[0],
            self._bounds.top + rel[1],
            self._bounds.width,
            self._bounds.height
        )

    def draw(self, surface):
        pygame.draw.rect(surface, color=self._colour, rect=self._bounds)
