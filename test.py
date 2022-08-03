import pygame


class Game(object):
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((200, 200))
        pygame.display.set_caption("tic-tac-toe online")
        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break

            self.screen.fill((255, 255, 255))

            keys = pygame.key.get_pressed()
            for i in range(97, 123):
                if keys[i]:
                    print(pygame.key.name(i))

            pygame.display.flip()
            self.clock.tick(30)

    pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()
