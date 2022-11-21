import pygame
from Setting import *
from PauseMenu import PauseMenu
import Level
import Menu
import FreeRun
class Game():
    def __init__(self):
        pygame.init()
        self.display=pygame.display.set_mode((WindowWidth,WindowHeight),flags=pygame.SCALED,vsync=1)
        pygame.display.set_caption("Swordman")
        # icon will be added here
        self.clock=pygame.time.Clock()
        self.running=True
        self.events=[]
        # first one for main menu and second one for pause third one for new level forth for free run
        # fifth for new free run
        self.levelTrue=[0,0,0,0,0]
        self.freeRun=FreeRun.FreeRun(self.display,self.levelTrue)
        self.level=Level.Level(self.display,self.levelTrue)
        self.menu=Menu.Menu(self.display,self.levelTrue)
        self.pauseMenu=PauseMenu(self.display,self.levelTrue)
    def update(self):
        while self.running:
            self.events=pygame.event.get()
            if self.levelTrue[0]==0 and self.levelTrue[3]==0:
                self.running = self.menu.menuLoop(self.events)
            if self.levelTrue[1]==1:
                self.running = self.pauseMenu.menuLoop(self.events)
            for event in self.events:
                if event.type==pygame.QUIT:
                    self.running=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        self.levelTrue[1]=1

            if self.levelTrue[0]==1:
                self.level.showAUpdate()
            if self.levelTrue[2]==1:
                self.level = Level.Level(self.display, self.levelTrue)
                self.levelTrue[2]=0
            if self.levelTrue[3]==1:
                self.freeRun.showAUpdate()
            if self.levelTrue[4]==1:
                self.freeRun=FreeRun.FreeRun(self.display,self.levelTrue)
                self.levelTrue[4] = 0
            pygame.display.flip()
            self.clock.tick(Fps)


game=Game()
game.update()
pygame.quit()