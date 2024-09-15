from src.view import View


class State:
    def __init__(self):
        self.hand = None
        self.ship = None
        self.view = View.MENU


state = State()
