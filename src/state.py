from src.models.button import Button
from src.models.card import Card
from src.models.enemy import Enemy


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
        self.enemies: list[Enemy] = []

        # ship
        self.ship: list = []

    def get_current_iter(self):
        for collection in self.current:
            for item in collection:
                yield item


state = State()
