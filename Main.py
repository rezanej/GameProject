import pygame
from Setting import *
import Level

import Menu

class Game():
    def __init__(self):
        pygame.init()
        self.display=pygame.display.set_mode((WindowWidth,WindowHeight),flags=pygame.SCALED,vsync=1)
        pygame.display.set_caption("Swordman")
        # icon will be added here
        self.clock=pygame.time.Clock()
        self.level=Level.Level(self.display)
        self.running=True
        self.events=[]
        self.levelTrue=[0]
        self.menu=Menu.Menu(self.display,self.levelTrue)

    def update(self):
        while self.running:
            self.events=pygame.event.get()
            if self.levelTrue[0]==0:
                self.running = self.menu.menuLoop(self.events)
            for event in self.events:
                if event.type==pygame.QUIT:
                    self.running=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        self.levelTrue[0]=0

            if self.levelTrue[0]==1:
               self.level.showAUpdate()
            pygame.display.flip()
            self.clock.tick(Fps)


game=Game()
game.update()
pygame.quit()