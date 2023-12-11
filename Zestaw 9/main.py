import pygame
import sys
from game import Game

def main() -> None:
    pygame.init()
    background_color = (0, 56, 71)

    screen = pygame.display.set_mode((300,600))
    pygame.display.set_caption("Tetris")

    clock = pygame.time.Clock()

    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move_left()
                if event.key == pygame.K_RIGHT:
                    game.move_right()
                if event.key == pygame.K_DOWN:
                    game.move_down()
                if event.key == pygame.K_UP:
                    game.rotate_block()
        screen.fill(background_color)
        game.draw(screen)
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()