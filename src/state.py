from src.view import View


class State:
    def __init__(self):
        # battle
        self.deck = None
        self.hand = None
        self.ship = None

        # ship
        self.crew = None

        # menu
        self.buttons = None

        # general
        self.view = View.MENU

    def view_setter(self, view):
        def inner():
            self.view = view

        return inner


state = State()
