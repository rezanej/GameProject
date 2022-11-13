import pygame
from Setting import *
from Player import *
from GrassTile import *

class Level():
    def __init__(self,display):
        self.initBackGround()
        self.tiles=pygame.sprite.Group()
        self.playerGroup=pygame.sprite.GroupSingle()
        self.display=display
        self.addTiles()
    def addTiles(self):
        r,c=0,0
        for tileNum in Level1TileMap:

            if tileNum=="1":
                self.tiles.add(GrassTile(c*64,r*64))
            if tileNum=="p":
                self.playerGroup.add(Player(c*64,r*64,self.tiles))
            elif tileNum=="n":
                r+=1
                c=-1
            c+=1
    def showAUpdate(self):
        self.scroll()
        self.tiles.update()
        self.display.blit(self.backGround,self.backGroundRect)
        self.tiles.draw(self.display)
        self.playerGroup.update()
        self.playerGroup.draw(self.display)

    def initBackGround(self):

        self.backGround = BackgroundImages[CurrentLevel]
        self.backGroundRect = self.backGround.get_rect()

    def scroll(self):
        if self.playerGroup.sprite.rect.x <WindowWidth/4 and self.playerGroup.sprite.direction.x<0:
            self.playerGroup.sprite.speed=0
            for tiles in self.tiles:
                tiles.rect.x+=PlayerSpeed
        elif self.playerGroup.sprite.rect.x >WindowWidth*(3/4) and self.playerGroup.sprite.direction.x>0:
            self.playerGroup.sprite.speed = 0
            for tiles in self.tiles:
                tiles.rect.x -= PlayerSpeed
        else:
            self.playerGroup.sprite.speed=PlayerSpeed


