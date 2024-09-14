import pygame

from src.card import Card, Hand
from src.event import EventHandler
from src.render import Renderer


def main():
    pygame.init()

    # Temporary card examples
    card1 = Card([50, 50])
    card2 = Card([150, 50])
    card3 = Card([250, 50])

    # TODO State handling? global cache?
    hand = Hand([card1, card2, card3])

    event_handler = EventHandler(hand=hand)
    renderer = Renderer(hand=hand)

    running = True
    while running:
        running = event_handler.step()
        renderer.render_frame()

    pygame.quit()


if __name__ == "__main__":
    main()
