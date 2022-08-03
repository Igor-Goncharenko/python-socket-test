import pygame
from search_game_menu import SearchGameMenu
from register_menu import RegisterMenu
from interface.constants import *
from interface.utils import thread_decorator


class Game(object):
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("tic-tac-toe online")
        self.clock = pygame.time.Clock()
        # menu init
        self.active_menu = 1
        self.register_menu = RegisterMenu()
        self.register_menu.play_button.func = self._play_button_func
        self.search_game_menu = SearchGameMenu()

    @thread_decorator
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break

            self.screen.fill(WHITE)

            if self.active_menu == 1:
                self.register_menu.draw()
            elif self.active_menu == 2:
                self.search_game_menu.draw()

            pygame.display.flip()
            self.clock.tick(FPS)

    def _play_button_func(self):
        user_name = self.register_menu.input_name.get_input()
        if user_name is not None and user_name != "":
            self.active_menu = 2
            print(user_name)


if __name__ == '__main__':
    game = Game()
    game.run().start()
