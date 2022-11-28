import pygame
from Setting import *
from PauseMenu import PauseMenu
import Level
import Menu
import FreeRun
import GameOver
import OptionMenu
class Game():
    def __init__(self):
        pygame.init()
        self.display=Display
        pygame.display.set_caption("Swordman")
        # icon will be added here
        self.clock=pygame.time.Clock()
        self.running=True
        self.events=[]
        # first one for main menu and second one for pause third one for new level forth for free run
        # fifth for new free run sixth one for gameover menu seventh for optionMenu Main 8th for optionMenu from pause
        self.levelTrue=[0,0,0,0,0,0,0,0]
        self.freeRun=FreeRun.FreeRun(self.display,self.levelTrue)
        self.level=Level.Level(self.display,self.levelTrue)
        self.menu=Menu.Menu(self.display,self.levelTrue)
        self.pauseMenu=PauseMenu(self.display,self.levelTrue)
        self.gameoverMenu=GameOver.GameoverMenu(self.display,self.levelTrue)
        self.optionMenu=OptionMenu.OptionMenu(self.display,self.levelTrue,self.level)
    def update(self):
        while self.running:
            self.events=pygame.event.get()
            self.eventsForQuit = self.events.copy()
            for event in self.events:
                if event.type==pygame.QUIT:
                    self.running=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        if self.levelTrue[1]==0 and self.levelTrue[0]==1 and self.levelTrue[6]==0:
                            self.levelTrue[1]=1
                            self.levelTrue[6]=0
                            self.levelTrue[7]=0
                        elif self.levelTrue[1]==0 and self.levelTrue[0]==1 and self.levelTrue[6]==1:
                            self.levelTrue[0]=0
                            self.levelTrue[6]=0
                            self.levelTrue[7]=0
                        elif self.levelTrue[1]==0 and self.levelTrue[0]==1:
                             self.levelTrue[0]=1
                             self.levelTrue[1]=1
                        elif self.levelTrue[1]==1 and self.levelTrue[0]==1:
                             self.levelTrue[0]=1
                             self.levelTrue[1]=0
                        elif self.levelTrue[3]==1:
                             self.levelTrue[0]=1
                             self.levelTrue[1]=1

            if self.levelTrue[0]==1 and self.levelTrue[6]==0:
                self.level.showAUpdate()

            if self.levelTrue[2]==1:
                self.level.reset()
                self.levelTrue[2]=0
                self.levelTrue[5]=0
            if self.levelTrue[3]==1:
                self.levelTrue[5]=0
                self.freeRun.showAUpdate()
            if self.levelTrue[4]==1:
                self.freeRun=FreeRun.FreeRun(self.display,self.levelTrue)
                self.levelTrue[4] = 0
            if self.levelTrue[0]==0 and self.levelTrue[3]==0 and self.levelTrue[6]==0 :
                self.running = self.menu.menuLoop(self.events)
                self.events=[]
            if self.levelTrue[1]==1:
                self.running = self.pauseMenu.menuLoop(self.events)
                self.events = []
            if self.levelTrue[5]==1:
                self.running =self.gameoverMenu.menuLoop(self.events)
                self.events = []
            if self.levelTrue[6]==1:
                self.optionMenu.menuLoop(self.events,0)
                self.events = []
            if self.levelTrue[7]==1:
                self.optionMenu.menuLoop(self.events,1)
                self.events = []
            # game was not able to quit while in menu so i added this
            for event in self.eventsForQuit:
                if event.type == pygame.QUIT:
                    self.running = False
            pygame.display.flip()
            self.clock.tick(Fps)


game=Game()
game.update()
pygame.quit()