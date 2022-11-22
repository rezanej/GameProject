import pygame
from Setting import *
from Kunai import *
from Player import *
from GrassTile import *
from Tree import *
from Tile import *
from Dog import *
from Light import Light
from Coin import Coin
class Level():
    def __init__(self,display,pause):
        self.initBackGround()
        self.pause=pause
        self.tiles=pygame.sprite.Group()
        self.subTiles=pygame.sprite.Group()
        self.playerGroup=pygame.sprite.GroupSingle()
        self.TreeGroup=pygame.sprite.Group()
        self.kunaiGroup=pygame.sprite.Group()
        self.borderGroup=pygame.sprite.Group()
        self.waterGroup=pygame.sprite.Group()
        self.enemyGroup=pygame.sprite.Group()
        self.lightGroup=pygame.sprite.Group()
        self.coinGroup=pygame.sprite.Group()
        self.display=display
        self.addTiles()
        self.x=0
        self.HudInit()
        self.HelthBar()
    def addTiles(self):
        r,c=0,0
        for tileNum in Level1TileMap:

            if tileNum=="1":
                self.tiles.add(GrassTile(c*64,r*64))
            elif tileNum=="p":
                self.playerGroup.add(Player(c*64,r*64,self.tiles,self.kunaiGroup,self.borderGroup,self.enemyGroup,self.coinGroup))
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
            elif tileNum=="D":
                self.enemyGroup.add(Dog(c*64,r*64,self.tiles))
            elif tileNum=="L":
                self.lightGroup.add(Light(c*64,r*64,1))
            elif tileNum=="c":
                self.coinGroup.add(Coin(c*64,r*64))
            c+=1
    def showAUpdate(self):
        if not self.pause[1]:
            self.scroll()
            self.tiles.update()
            self.display.blit(self.backGround,self.backGroundRect)
            self.tiles.draw(self.display)
            self.TreeGroup.draw(self.display)
            self.subTiles.draw(self.display)
            self.kunaiGroup.update()
            self.kunaiGroup.draw(self.display)
            self.playerGroup.update(self.tiles)
            self.playerGroup.draw(self.display)
            self.coinGroup.update()
            self.coinGroup.draw(self.display)
            self.enemyGroup.update()
            self.enemyGroup.draw(self.display)
            self.HudUpdate()
            self.HudBlit()
            # self.night()
            # self.blitNight()
            # self.lightGroup.draw(self.display)

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
            for tiles in self.enemyGroup:
                tiles.rect.x+=PlayerSpeed
            for tiles in self.lightGroup:
                tiles.rect.x+=PlayerSpeed
            for tiles in self.coinGroup:
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
            for tiles in self.enemyGroup:
                tiles.rect.x-=PlayerSpeed
            for tiles in self.lightGroup:
                tiles.rect.x-=PlayerSpeed
            for tiles in self.coinGroup:
                tiles.rect.x-=PlayerSpeed
        else:
            self.playerGroup.sprite.speed=PlayerSpeed
    def HudInit(self):
        self.font=HudFont
        self.healthText=self.font.render("Health:",True,(255,0,0))
        self.healthTextRect=self.healthText.get_rect(topleft=(20,23))
        self.kunaiImage=pygame.transform.scale(pygame.image.load("PlayerImages/Kunai.png"),(16/1.3,80/1.3))
        self.kunaiImageRect=KunaiImgae.get_rect(topleft=(20,70))
        self.kunaiText=self.font.render(f": {self.playerGroup.sprite.kunaiNumber}",True,(40,54,67))
        self.kunaiTextRect=self.kunaiText.get_rect(topleft=(50,85))
        self.scoreText=self.font.render(f"Score: {self.playerGroup.sprite.score}",True,((40,54,67)))
        self.scoreTextRect=self.scoreText.get_rect(topleft=(350,23))
    def HelthBar(self):
        self.helthBar=pygame.surface.Surface((200,16))
        self.helthBar.fill((0,156,56))
        self.helthBarRect=self.helthBar.get_rect(topleft=(120,34))
        self.helthBarBackground=pygame.rect.Rect(120,34,200,16)
    def HudBlit(self):
        self.display.blit(self.healthText, self.healthTextRect)
        self.display.blit(self.helthBar,self.helthBarRect)
        pygame.draw.rect(self.display,(255,140,9),self.helthBarBackground,3)
        self.display.blit(self.kunaiImage,self.kunaiImageRect)
        self.display.blit(self.kunaiText,self.kunaiTextRect)
        self.display.blit(self.scoreText,self.scoreTextRect)
        # self.display.blit(self.vintageImage,self.vintageImageRect)
    def HudUpdate(self):
        self.helthBar=pygame.surface.Surface((self.playerGroup.sprite.health*2,16))
        self.scoreText = self.font.render(f"Score: {self.playerGroup.sprite.score}", True, ((40, 54, 67)))
        self.kunaiText = self.font.render(f": {self.playerGroup.sprite.kunaiNumber}", True, (40, 54, 67))
    def vintage(self):
        self.vintageImage=pygame.transform.scale(pygame.image.load("vintage2.jpg").convert_alpha(),(WindowWidth,WindowHeight))
        self.vintageImageRect=self.vintageImage.get_rect()
        alpha = 60
        self.vintageImage.fill((255, 255, 255, alpha), None, pygame.BLEND_RGBA_MULT)
    def night(self):
        self.fog=pygame.surface.Surface((WindowWidth,WindowHeight))
        self.fog.fill((30,30,30))
        self.fogRect=self.fog.get_rect(topleft=(0,0))

    def blitNight(self):
        self.display.blit(self.fog,self.fogRect,special_flags=pygame.BLEND_MULT)
    def reset(self):
        self.__init__(self.display,self.pause)