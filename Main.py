import pygame
from Setting import *


class Game():
    def __init__(self):
        pygame.init()
        self.display=pygame.display.set_mode((WindowWidth,WindowHeight),flags=pygame.SCALED,vsync=1)
        pygame.display.set_caption("Swordman")
        # icon will be added here
        self.clock=pygame.time.Clock()

        self.running=True

    def update(self):
        while self.running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.running=False


            pygame.display.flip()
            self.clock.tick(Fps)


game=Game()
game.update()
pygame.quit()