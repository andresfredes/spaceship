from random import randint

import pygame

from src.settings import settings
from src.colours import Colour
from src.card import Card, Hand


def main():
    pygame.init()
    screen = pygame.display.set_mode(
        (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
    )
    background = pygame.Surface(screen.get_size()).convert()

    clock = pygame.time.Clock()
    running = True

    stars = [
        [
            randint(0, settings.SCREEN_WIDTH),
            randint(0, settings.SCREEN_HEIGHT)
        ]
        for _ in range(settings.NUM_STARS)
    ]

    card1 = Card([50, 50])
    card2 = Card([150, 50])
    card3 = Card([250, 50])
    hand = Hand([card1, card2, card3])

    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    hand.hold_card(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    hand.unhold_card()
            if event.type == pygame.MOUSEMOTION:
                hand.move_held_card(event.rel)
            if event.type == pygame.QUIT:
                running = False

        background.fill(Colour.BLACK.value)

        for star in stars:
            pygame.draw.line(background, Colour.WHITE.value, star, star)
            star[0] = star[0] - 1
            if star[0] < 0:
                star[0] = settings.SCREEN_WIDTH
                star[1] = randint(0, settings.SCREEN_HEIGHT)

        hand.draw(background)

        screen.blit(background, (0, 0))
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
