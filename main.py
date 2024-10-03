from src.loop import GameLoop
from src.models.button import Button
from src.models.card import Card
from src.models.ship import Ship
from src.state import state
from src.view import View


def main():
    # handle pygame context
    with GameLoop() as loop:

        # Set up initial game state
        card1 = Card(pos=[350, 500], title="Stan", text="This is example text")
        card2 = Card(pos=[550, 500], title="Amy", text="Some more text")
        card3 = Card(pos=[750, 500], title="Rob", text="And another card text")
        for card in [card1, card2, card3]:
            state.add(card)

        ship = Ship()
        state.ship = ship

        buttons = [
            Button(pos=[350, 200], text="SHIP", action=state.view_setter(View.SHIP)),
            Button(
                pos=[750, 200], text="BATTLE", action=state.view_setter(View.BATTLE)
            ),
        ]
        state.buttons = buttons

        # Run game
        loop.run()


if __name__ == "__main__":
    main()
