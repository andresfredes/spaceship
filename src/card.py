import pygame
import pygame.freetype

from src.colours import Colour
from src.settings import settings


class Deck:
    def __init__(self):
        self._cards = []


class Discard:
    def __init__(self):
        self._cards = []


class Hand:
    def __init__(self, cards=[]):
        self._cards = cards
        self.held_card_index = None

    def __iter__(self):
        for card in self._cards:
            yield card

    def hold_card(self, pos):
        for i, card in enumerate(self._cards):
            if card.collidepoint(pos):
                card.mouse_held = True
                self.held_card_index = i

    def unhold_card(self):
        if self.held_card_index is None:
            return
        self._cards[self.held_card_index].mouse_held = False
        self.held_card_index = None

    def move_held_card(self, rel):
        if self.held_card_index is None:
            return
        self._cards[self.held_card_index].move(rel)

    def draw(self, surface):
        for card in self._cards:
            card.draw(surface)

    def add(self, cards):
        if isinstance(cards, list):
            for card in cards:
                self._cards.append(card)
        else:
            self._cards.append(cards)


class Card:
    def __init__(self, pos=[0, 0], title="", text=""):
        self.mouse_held = False

        self._pos = pos
        self._title = title
        self._text = text

        self._width = settings.CARD_WIDTH
        self._height = settings.CARD_HEIGHT
        self._colour = Colour.WHITE.value
        self._text_colour = Colour.BLACK.value

        self._font = pygame.freetype.SysFont(
            pygame.freetype.get_default_font(), settings.FONT_SIZE
        )
        self._surface = pygame.Surface((self._width, self._height))
        self._bounds = self._surface.get_rect()
        self.move((0, 0))

        self._surface.fill(self._colour)
        self._font.render_to(
            surf=self._surface,
            dest=(10, 10),
            text=self._title,
            fgcolor=self._text_colour,
        )
        self._font.render_to(
            surf=self._surface,
            dest=(10, 100),
            text=self._text,
            fgcolor=self._text_colour,
        )

    def collidepoint(self, pos):
        return self._bounds.collidepoint(pos)

    def move(self, rel):
        self._pos = (self._pos[0] + rel[0], self._pos[1] + rel[1])
        self._bounds.update(
            self._pos[0],
            self._pos[1],
            self._bounds.width,
            self._bounds.height,
        )

    def draw(self, surface):
        surface.blit(self._surface, self._pos)
