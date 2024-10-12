from random import shuffle

from src.enums import View
from src.models.button import Button
from src.models.card import Card
from src.models.ship import Ship
from src.state import state


def start_game():
    state.cards = [
        Card(pos=[350, 500], title="Stan", text="This is example text"),
        Card(pos=[550, 500], title="Amy", text="Some more text"),
        Card(pos=[750, 500], title="Rob", text="And another card text"),
    ]
    state.ship = [Ship()]
    state.buttons = [
        Button(pos=[350, 200], text="SHIP", action=view_changer(View.SHIP)),
        Button(pos=[750, 200], text="BATTLE", action=view_changer(View.BATTLE)),
    ]
    view_changer(View.MENU)()


def reshuffle(deck: list[Card], discard: list[Card]) -> list[Card]:
    return shuffle([*deck, *discard])


def view_changer(view: View):
    def inner():
        match view:
            case View.MENU:
                state.current = [state.buttons]
            case View.BATTLE:
                state.current = [state.cards]
            case View.SHIP:
                state.current = [state.ship]
            case _:
                print("unhandled view type")

    return inner
