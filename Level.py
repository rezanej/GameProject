import pygame
from Setting import *
from Kunai import *
from Player import *
from GrassTile import *
from Tree import *
from Tile import *
class Level():
    def __init__(self,display):
        self.initBackGround()
        self.tiles=pygame.sprite.Group()
        self.subTiles=pygame.sprite.Group()
        self.playerGroup=pygame.sprite.GroupSingle()
        self.TreeGroup=pygame.sprite.Group()
        self.kunaiGroup=pygame.sprite.Group()
        self.borderGroup=pygame.sprite.Group()
        self.waterGroup=pygame.sprite.Group()
        self.display=display
        self.addTiles()
        self.x=0
    def addTiles(self):
        r,c=0,0
        for tileNum in Level1TileMap:

            if tileNum=="1":
                self.tiles.add(GrassTile(c*64,r*64))
            elif tileNum=="p":
                self.playerGroup.add(Player(c*64,r*64,self.tiles,self.kunaiGroup,self.borderGroup))
            elif tileNum=="n":
                r+=1
                c=-1
            elif tileNum=="t":
                self.TreeGroup.add(Tree(TreeImages[0],c*64,r*64+64))
            elif tileNum=="T":
                self.TreeGroup.add(Tree(TreeImages[1],c*64,r*64+64))
            elif tileNum=="d":
                self.tiles.add(Tile(c*64,r*64,DirtImages[0]))
            elif tileNum=="b":
                self.borderGroup.add(Tile(c*64,r*64,DirtImages[0]))
            elif tileNum=="w":
                self.subTiles.add(Tile(c*64,r*64,WaterImages[0]))
            elif tileNum=="W":
                self.subTiles.add(Tile(c*64,r*64,WaterImages[1]))
            c+=1
    def showAUpdate(self):
        self.scroll()
        self.tiles.update()
        self.display.blit(self.backGround,self.backGroundRect)
        self.tiles.draw(self.display)
        self.TreeGroup.draw(self.display)
        self.subTiles.draw(self.display)
        self.kunaiGroup.update()
        self.kunaiGroup.draw(self.display)
        self.playerGroup.update()
        self.playerGroup.draw(self.display)


    def initBackGround(self):

        self.backGround = BackgroundImages[CurrentLevel]
        self.backGroundRect = self.backGround.get_rect()

    def scroll(self):
        if self.playerGroup.sprite.rect.x <WindowWidth/4 and self.playerGroup.sprite.direction.x<0:
            self.x-=1
            self.playerGroup.sprite.speed=0
            for tiles in self.tiles:
                tiles.rect.x+=PlayerSpeed
            for tiles in self.TreeGroup:
                tiles.rect.x+=PlayerSpeed
            for tiles in self.subTiles:
                tiles.rect.x+=PlayerSpeed
            for tiles in self.borderGroup:
                tiles.rect.x+=PlayerSpeed
        elif self.playerGroup.sprite.rect.x >WindowWidth*(3/4) and self.playerGroup.sprite.direction.x>0:
            self.x+=1
            self.playerGroup.sprite.speed = 0
            for tiles in self.tiles:
                tiles.rect.x -= PlayerSpeed
            for tiles in self.TreeGroup:
                tiles.rect.x-=PlayerSpeed
            for tiles in self.subTiles:
                tiles.rect.x-=PlayerSpeed
            for tiles in self.borderGroup:
                tiles.rect.x-=PlayerSpeed
        else:
            self.playerGroup.sprite.speed=PlayerSpeed


