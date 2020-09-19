import pygame
from tresenraya.constants import WIDTH, HEIGHT, SQUARE_SIZE
from tresenraya.game import Game

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Tres en raya')

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        game.update()

    pygame.quit()

main()