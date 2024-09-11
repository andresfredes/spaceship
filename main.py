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

    square = pygame.Rect(50, 50, 50, 50)
    clickables = [{"shape": square, "clicked": False}]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for item in clickables:
                        if item["shape"].collidepoint(event.pos):
                            item["clicked"] = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    for item in clickables:
                        if item["clicked"]:
                            item["clicked"] = False
            if event.type == pygame.MOUSEMOTION:
                for item in clickables:
                    if item["clicked"]:
                        item["shape"].update(
                            square.left + event.rel[0],
                            square.top + event.rel[1],
                            square.width,
                            square.height
                        )
            if event.type == pygame.QUIT:
                running = False
        
        background.fill(Colour.BLACK.value)

        for star in stars:
            pygame.draw.line(background, Colour.WHITE.value, star, star)
            star[0] = star[0] - 1
            if star[0] < 0:
                star[0] = settings.SCREEN_WIDTH
                star[1] = randint(0, settings.SCREEN_HEIGHT)
            
        pygame.draw.rect(background, color=Colour.WHITE.value, rect=square)

        screen.blit(background, (0, 0))
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
