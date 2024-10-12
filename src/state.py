from random import shuffle

from src.models.button import Button
from src.models.card import Card


def reshuffle(deck: list[Card], discard: list[Card]) -> list[Card]:
    shuffled = [*deck, *discard]
    return shuffle(shuffled)


class State:
    def __init__(self):
        self.cards: list[Card] = []

        # general
        self.current: list[list] = []

        # menu
        self.buttons: list[Button] = []

        # battle
        self.deck: list[Card] = []
        self.discard: list[Card] = []
        self.hand: list[Card] = []

        # ship
        self.ship: list = []


state = State()
