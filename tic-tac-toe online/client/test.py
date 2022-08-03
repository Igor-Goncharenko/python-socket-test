import pygame

from interface.constants import *
from interface.button import DefaultButton
from interface.input_label import InputLabel
from register_menu import RegisterMenu
from search_game_menu import SearchGameMenu, JoinGameBlock
from interface.scrollable_window import ScrollableWindow, ScrollableWindowBlock


class Game(object):
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("tic-tac-toe online")
        self.clock = pygame.time.Clock()
        import random
        self.menu = SearchGameMenu("Igor")
        self.menu.games.blocks = [
            JoinGameBlock(game_name=str(random.randint(100, 10000)), user_name=str(i), opened=True)
            for i in range(30)
        ]

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        self.menu.games.scroll(up=True)
                    elif event.button == 5:
                        self.menu.games.scroll(down=True)

            self.screen.fill(WHITE)

            self.menu.draw()

            pygame.display.flip()
            self.clock.tick(FPS)

    pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()
