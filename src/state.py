from src.view import View


class State:
    def __init__(self):
        # battle
        self.deck = None
        self.hand = None
        self.ship = None

        # ship
        self.crew = None

        # general
        self.view = View.SHIP


state = State()
