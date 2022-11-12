import pygame
from Setting import *
from Player import *
from GrassTile import *

class Level():
    def __init__(self,display):
        self.initBackGround()
        self.tiles=pygame.sprite.Group()
        self.display=display
        self.addTiles()
    def addTiles(self):
        r,c=0,0
        for tileNum in Level1TileMap:

            if tileNum=="1":
                self.tiles.add(GrassTile(c*64,r*64))
            elif tileNum=="n":
                r+=1
                c=-1
            c+=1
        print(self.tiles.sprites())
    def show(self):
        self.tiles.update()
        self.display.blit(self.backGround,self.backGroundRect)
        self.tiles.draw(self.display)
    def initBackGround(self):
        self.backGround = BackgroundImages[CurrentLevel]
        self.backGroundRect = self.backGround.get_rect()

