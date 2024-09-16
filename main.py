from src.card import Card, Hand
from src.loop import GameLoop
from src.ship import Ship
from src.state import state


def main():
    with GameLoop() as loop:

        # Set up initial game state
        card1 = Card(pos=[350, 500], title="Stan", text="This is example text")
        card2 = Card(pos=[550, 500], title="Amy", text="Some more text")
        card3 = Card(pos=[750, 500], title="Rob", text="And another card text")
        hand = Hand([card1, card2, card3])
        ship = Ship()
        state.hand = hand
        state.ship = ship

        # Run game
        loop.run()


if __name__ == "__main__":
    main()
