import random

import pygame

import Tree
from Tile import Tile
from Setting import *
from GrassTile import GrassTile
from Player import Player
from Coin import Coin
from Heart import Heart
class FreeRun:
    def __init__(self,display,pause):
        self.initBackGround()
        self.pause=pause
        self.tiles=pygame.sprite.Group()
        self.subTiles=pygame.sprite.Group()
        self.playerGroup=pygame.sprite.GroupSingle()
        self.TreeGroup=pygame.sprite.Group()
        self.waterGroup=pygame.sprite.Group()
        self.enemyGroup=pygame.sprite.Group()
        self.lightGroup=pygame.sprite.Group()
        self.coinGroup=pygame.sprite.Group()
        self.heartGroup=pygame.sprite.Group()
        self.display=display
        self.lastTileY = 0
        self.t=[]
        self.initTiles()
        self.y=0
        self.HudInit()
        self.HelthBar()
        self.playerGroup.sprite.speed = 0
        self.addScorSpeed=0.1
    def initTiles(self):
        r, c = 0, 0
        for tileNum in FreeRunStart:

            if tileNum == "1":
                g=GrassTile(c * 64, r * 64,0)
                self.tiles.add(g)
                self.t.append(g)
                self.lastTileY = r*64
            elif tileNum == "p":
                self.playerGroup.add(Player(c * 64, r * 64, self.tiles,coinGroup=self.coinGroup,heartGroup=self.heartGroup))
            elif tileNum == "d":
                g=Tile(c * 64, r * 64, DirtImages[0])
                self.tiles.add(g)
                self.t.append(g)
            elif tileNum == "n":
                r += 1
                c = -1

            c += 1

    def addTiles(self):
        r, c = self.lastTileY//64, 20
        count=0
        j=random.randint(4, 10)

        for i in range(j):

            if r>=8:
                r = r + -2
            elif r<=3:
                r = r + random.choice([1, 2])
            else :
                r = r + random.choice([1, 2,-2])
            ct = random.randint(4, 10)
            for i in range(ct):
                treePosibility = random.choice([1, 0, 0, 0, 0, 0, 0,0,0,0,0,0, 0, 0])
                objectPosibility=random.choice([1, 0, 0, 0, 0, 0, 0,0,0,0,0,0, 0, 0])
                coinPosibility=random.choice([1, 1,1,1,0,0,0,0,0,0,0,0])
                heartPosibility=random.choice([1, 0, 0, 0, 0, 0, 0,0,0,0,0,0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0])
                for a in range(10-r):
                    d=Tile((c+i)*64,(r+a)*64,DirtImages[0])
                    self.tiles.add(d)
                    self.t.append(d)
                if treePosibility and (i!=0 and i!=ct-1):
                    treeImageRand=random.choice([0,1,1,1,1,1,1,0,0])
                    self.TreeGroup.add(Tree.Tree(TreeImages[treeImageRand],(c+i)*64,(r-1)*64+64))
                if objectPosibility and (i!=0 and i!=ct-1):
                    objectImageRand=random.randint(0,4)
                    g=Tile((c+i)*64,(r-1)*64+24,ObjectImages[objectImageRand])
                    self.tiles.add(g)
                    self.t.append(g)
                if coinPosibility:
                    a=random.choice([0,1,2,3])
                    g=random.choice([Coin((c+i)*64,(r-1-a)*64,self.playerGroup,10,CoinImages),Coin((c+i)*64,(r-1)*64,self.playerGroup,30,GoldCoinImages)])
                    self.coinGroup.add(g)
                if heartPosibility:
                    a = random.choice([0, 1, 2, 3])
                    g =Heart((c+i)*64,(r-1-a)*64,self.playerGroup,20)
                    self.heartGroup.add(g)
                g=GrassTile((c+i)*64,r*64,0)
                self.tiles.add(g)
                self.t.append(g)
                count+=1
                if count==20:
                    self.lastTileY=g.rect.y
                    return 0
            c+=ct
    def deletetiles(self):
        tiles=pygame.sprite.Group()
        t=[]
        for i in self.t:
            if i.rect.x>-64:
                t.append(i)
        for i in t:
            tiles.add(t)
        for i in self.coinGroup:
            if i.rect.x<-80:
                i.kill()
        self.tiles=tiles
        self.t=t
        for i in self.TreeGroup:
            if i.rect.x<-80:
                i.kill()
    def checkDeleteandAdd(self):
        if self.t[0].rect.x<=-WindowWidth:
            self.tileNumber = random.randint(10, 30)
            self.addTiles()
            self.deletetiles()
    def showAUpdate(self):

        if not self.pause[1]:
            self.checkDeleteandAdd()
            self.scroll()
            self.tiles.update()
            self.display.blit(self.backGround,self.backGroundRect)
            self.tiles.draw(self.display)
            self.TreeGroup.draw(self.display)
            self.subTiles.draw(self.display)
            self.playerGroup.update(self.tiles)
            self.playerGroup.draw(self.display)
            self.enemyGroup.update()
            self.enemyGroup.draw(self.display)
            self.coinGroup.update()
            self.coinGroup.draw(self.display)
            self.heartGroup.update()
            self.heartGroup.draw(self.display)
            self.HudBlit()
            self.HudUpdate()
            self.checkGameOver()
            self.addScore()

            # self.night()
            # self.blitNight()
            # self.lightGroup.draw(self.display)
    def initBackGround(self):

        self.backGround = BackgroundImages[CurrentLevel]
        self.backGroundRect = self.backGround.get_rect()

    def scroll(self):
        if not self.playerGroup.sprite.dead:
            for tiles in self.tiles:
                tiles.rect.x-=PlayerSpeed
            for tiles in self.TreeGroup:
                tiles.rect.x-=PlayerSpeed
            for tiles in self.subTiles:
                tiles.rect.x-=PlayerSpeed

            for tiles in self.enemyGroup:
                tiles.rect.x-=PlayerSpeed
            for tiles in self.lightGroup:
                tiles.rect.x-=PlayerSpeed
            for tiles in self.coinGroup:
                tiles.rect.x -= PlayerSpeed
            for tiles in self.heartGroup:
                tiles.rect.x -= PlayerSpeed

    def HudInit(self):
        self.font=HudFont
        self.healthText=self.font.render("health:",True,(255,0,0))
        self.healthTextRect=self.healthText.get_rect(topleft=(20,23))
        self.scoreText = self.font.render(f"Score: {int(self.playerGroup.sprite.score)}", True, ((40, 54, 67)))
        self.scoreTextRect = self.scoreText.get_rect(topleft=(350, 23))

    def HelthBar(self):
        self.helthBar = pygame.surface.Surface((200, 16))
        self.helthBar.fill((0, 156, 56))
        self.helthBarRect = self.helthBar.get_rect(topleft=(120, 34))
        self.helthBarBackground = pygame.rect.Rect(120, 34, 200, 16)
    def HudBlit(self):
        self.display.blit(self.healthText, self.healthTextRect)
        self.display.blit(self.helthBar,self.helthBarRect)
        pygame.draw.rect(self.display,(255,140,9),self.helthBarBackground,3)
        self.display.blit(self.scoreText, self.scoreTextRect)
        # self.display.blit(self.vintageImage,self.vintageImageRect)

    def HudUpdate(self):
        if self.playerGroup.sprite.health<=0:
            self.playerGroup.sprite.health=0
        self.helthBar=pygame.surface.Surface((self.playerGroup.sprite.health*2,16))
        self.scoreText = self.font.render(f"Score: {int(self.playerGroup.sprite.score)}", True, ((40, 54, 67)))

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
    def checkGameOver(self):
        if self.playerGroup.sprite.health==0:
            self.pause[5]=1
            self.playerGroup.sprite.freeRun=False
            self.playerGroup.sprite.die()
    def addScore(self):
        if self.playerGroup.sprite.dead==False:
            self.playerGroup.sprite.score+=self.addScorSpeed