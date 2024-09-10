from random import randint

import pygame

from src.settings import settings
from src.colours import Colour


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

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        background.fill(Colour.BLACK.value)

        for star in stars:
            pygame.draw.line(background, Colour.WHITE.value, star, star)
            star[0] = star[0] - 1
            if star[0] < 0:
                star[0] = settings.SCREEN_WIDTH
                star[1] = randint(0, settings.SCREEN_HEIGHT)

        screen.blit(background, (0, 0))
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
