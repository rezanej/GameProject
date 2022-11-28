import pygame

import Kunai
from Setting import *
from Kunai import *
from Player import *
from GrassTile import *
from Tree import *
from Tile import *
from Enemy import *
from Light import Light
from Coin import Coin
from Heart import Heart
from NinjaGirl import NinjaGirl
from os import remove
from OptionMenu import OptionMenu
import Portal
from Zombie import Zombie
class Level():
    def __init__(self,display,pause):
        self.currentLevel=0
        self.setLevel()
        self.initBackGround()
        self.pause=pause
        self.tiles=pygame.sprite.Group()
        self.subTiles=pygame.sprite.Group()
        self.playerGroup=pygame.sprite.GroupSingle()
        self.treeAndObjectGroup=pygame.sprite.Group()
        self.kunaiGroup=pygame.sprite.Group()
        self.borderGroup=pygame.sprite.Group()
        self.waterGroup=pygame.sprite.Group()
        self.enemyGroup=pygame.sprite.Group()
        self.lightGroup=pygame.sprite.Group()
        self.coinGroup=pygame.sprite.Group()
        self.fightBorder=pygame.sprite.Group()
        self.checkpoints=pygame.sprite.Group()
        self.heartGroup=pygame.sprite.Group()
        self.portalGroup=pygame.sprite.Group()
        self.display=display
        self.x=0
        self.addTiles()
        self.addKunai()
        self.lastCheckPoint=[0,0]
        self.loadSave()
        self.loadCheckpoint()
        self.HudInit()
        self.HelthBar()
        self.playMusic()
    def setLevel(self):
        if exists("save.txt"):
            with  open("save.txt", "r") as SaveFile:
                self.currentLevel = int(SaveFile.readline())
    def loadSave(self):
        if exists("save.txt"):
            with  open("save.txt", "r") as SaveFile:
                self.currentLevel = int(SaveFile.readline())
                LastCheckpoint = SaveFile.readline().split(",")
                self.lastCheckPoint[0] = int(LastCheckpoint[0])
                self.lastCheckPoint[1] = int(LastCheckpoint[1])
                self.playerGroup.sprite.score = int(SaveFile.readline())
                self.playerGroup.sprite.kunaiNumber = int(SaveFile.readline())
                self.playerGroup.sprite.health = int(SaveFile.readline())
                if int(SaveFile.readline())==0:
                    OptionMenu.PlayMusic=False
                else :OptionMenu.PlayMusic=True
            if self.playerGroup.sprite.health==0:
                remove("save.txt")
                self.reset()
        else:
            with  open("save.txt", "a") as SaveFile:

                # level , last checkpoint ,score,kunai number,health
                SaveFile.write(f"{self.currentLevel}")
                SaveFile.write("\n")
                SaveFile.write("0,0\n")
                SaveFile.write("0\n")
                SaveFile.write(f"{self.playerGroup.sprite.kunaiNumber}")
                SaveFile.write("\n")
                SaveFile.write("100")
                SaveFile.write("\n")
                SaveFile.write("0")
    def loadCheckpoint(self):
        for checkpoint in self.checkpoints:
            if checkpoint.rect.x==self.lastCheckPoint[0] and checkpoint.rect.y==self.lastCheckPoint[1]:
                self.playerGroup.sprite.rect.topleft=checkpoint.rect.topleft
                self.scrollToPlayer(-(self.playerGroup.sprite.rect.x - 500))
                self.lastCheckPoint=[self.playerGroup.sprite.rect.x,self.playerGroup.sprite.rect.y]
        for coin in self.coinGroup:
            if coin.rect.x<self.lastCheckPoint[0]:
                coin.kill(0)
        for enemy in self.enemyGroup:
            if enemy.rect.x<self.lastCheckPoint[0]:
                enemy.kill()
        for heart in self.heartGroup:
             if heart.rect.x<self.lastCheckPoint[0]:
                 heart.kill(0)
        for kunai in self.kunaiGroup:
             if kunai.rect.x<self.lastCheckPoint[0]:
                 kunai.kill()

    def addTiles(self):
        r,c=0,0
        for tileNum in LevelMaps[self.currentLevel]:

            if tileNum=="1":
                self.tiles.add(GrassTile(c*64,r*64,self.currentLevel))
            elif tileNum=="p":
                self.playerGroup.add(Player(c*64,r*64,self.tiles,self.kunaiGroup,self.borderGroup,self.enemyGroup,\
                                            self.coinGroup,self.fightBorder,self.checkpoints,self.heartGroup))
            elif tileNum=="n":
                r+=1
                c=-1
            elif tileNum=="t":
                self.treeAndObjectGroup.add(Tree(TreeImages[0],c*64,r*64+64))
            elif tileNum=="T":
                self.treeAndObjectGroup.add(Tree(TreeImages[1],c*64,r*64+64))
            elif tileNum=="e":
                self.treeAndObjectGroup.add(Tree(TreeImages[3],c*64,r*64+74))
            elif tileNum=="j":
                self.treeAndObjectGroup.add(Tree(TreeImages[4],c*64,r*64+74))
            elif tileNum=="2":
                self.treeAndObjectGroup.add(Tile(c*64,r*64,ObjectImages[7]))
            elif tileNum=="3":
                self.treeAndObjectGroup.add(Tile(c*64,r*64+10,ObjectImages[6]))
            elif tileNum=="4":
                self.treeAndObjectGroup.add(Tile(c*64,r*64,ObjectImages[5]))
            elif tileNum=="5":
                self.treeAndObjectGroup.add(Tree(TreeImages[5],c*64,r*64+74))
            elif tileNum=="d":
                self.tiles.add(Tile(c*64,r*64,DirtImages[self.currentLevel]))
            elif tileNum=="b":
                self.borderGroup.add(Tile(c*64,r*64,DirtImages[0]))
            elif tileNum=="B":
                self.fightBorder.add(Tile(c*64,r*64,DirtImages[0]))
            elif tileNum=="w":
                self.subTiles.add(Tile(c*64,r*64,WaterImages[0]))
            elif tileNum=="W":
                self.subTiles.add(Tile(c*64,r*64,WaterImages[1]))
            elif tileNum=="D":
                self.enemyGroup.add(Enemy(c*64,r*64,DogSpeed,self.tiles,self.playerGroup,self.fightBorder,DogIdleImages\
                                          ,DogRunImages,DogDeadImages,DogIdleImagesLeft,DogRunImagesLeft,DogDeadImagesLeft))
            elif tileNum=="a":
                self.enemyGroup.add(Enemy(c * 64, r * 64, DogSpeed, self.tiles, self.playerGroup, self.fightBorder, CatIdleImages\
                          , CatRunImages, CatDeadImages, CatIdleImagesLeft, CatRunImagesLeft, CatDeadImagesLeft))
            elif tileNum=="N":
                self.enemyGroup.add(NinjaGirl(c * 64, r * 64, DogSpeed, self.tiles, self.playerGroup, self.fightBorder, NinjaGirlIdleImages\
                          , NinjaGirlRunImages, NinjaGirlDeadImages, NinjaGirlIdleImagesLeft, NinjaGirlRunImagesLeft, NinjaGirlDeadImagesLeft,\
                            NinjaGirlThrowImages,NinjaGirlThrowImagesLeft,self.kunaiGroup ))
            elif tileNum=="Z":
                self.enemyGroup.add(Zombie(c * 64, r * 64, DogSpeed, self.tiles, self.playerGroup, self.fightBorder, zombieMaleIdleImages\
                          , zombieMaleWalkImages, zombieMaleDeadImages, zombieMaleIdleImagesLeft, zombieMaleWalkImagesLeft, zombieMaleDeadImagesLeft))
            elif tileNum=="z":
                self.enemyGroup.add(Zombie(c * 64, r * 64, DogSpeed, self.tiles, self.playerGroup, self.fightBorder,zombieFemaleIdleImages \
                                           , zombieFemaleWalkImages, zombieFemaleDeadImages, zombieFemaleIdleImagesLeft,zombieFemaleWalkImagesLeft, zombieFemaleDeadImagesLeft))
            elif tileNum=="L":
                self.lightGroup.add(Light(c*64,r*64,1))
            elif tileNum=="P":
                self.treeAndObjectGroup.add(Tree(TreeImages[2], c * 64, r * 64 + 74))
                self.checkpoints.add(Tile(c*64,r*64,DirtImages[0]))
            elif tileNum=="c":
                self.coinGroup.add(Coin(c*64,r*64,self.playerGroup,10,CoinImages))
            elif tileNum=="C":
                self.coinGroup.add(Coin(c*64,r*64,self.playerGroup,20,GoldCoinImages))
            elif tileNum=="h":
                self.heartGroup.add(Heart(c*64,r*64,self.playerGroup,20))
            elif tileNum=="o":
                self.portalGroup.add(Portal.Portal(PortalImages,c*64,r*64,self.playerGroup,self))
            c+=1
    def addKunai(self):
        r, c = 0, 0
        for tileNum in LevelMaps[self.currentLevel]:
            if tileNum=="n":
                r += 1
                c = -1
            elif tileNum == "k":
                self.kunaiGroup.add(Kunai(c * 64 + 20, r * 64 + 50, self.playerGroup.sprite, self.enemyGroup, 0, True))
            c+=1
    def showAUpdate(self):
        if not self.pause[1] and not self.pause[7]:
            self.scroll()
            self.tiles.update()
            self.display.blit(self.backGround,self.backGroundRect)
            self.treeAndObjectGroup.draw(self.display)
            self.tiles.draw(self.display)
            self.subTiles.draw(self.display)
            self.kunaiGroup.update()
            self.kunaiGroup.draw(self.display)
            self.playerGroup.update(self.tiles) # self.tiles are for falling problem in freeRun
            self.playerGroup.draw(self.display)
            self.coinGroup.update()
            self.coinGroup.draw(self.display)
            self.enemyGroup.update()
            self.enemyGroup.draw(self.display)
            self.heartGroup.update()
            self.heartGroup.draw(self.display)
            self.portalGroup.update(self)
            self.portalGroup.draw(self.display)
            self.HudUpdate()
            self.HudBlit()
            self.enemyShowHealth()
            self.fallingFromScreen(self.playerGroup.sprite)
            self.setCheckPoint()
            self.checkGameOver()
            if self.currentLevel==2:
                self.night()
                self.blitNight()
                self.lightGroup.draw(self.display)
    def initBackGround(self):

        self.backGround = BackgroundImages[self.currentLevel]
        self.backGroundRect = self.backGround.get_rect()

    def scroll(self):
        if self.playerGroup.sprite.rect.x <WindowWidth/4 and self.playerGroup.sprite.direction.x<0:
            self.x+=PlayerSpeed
            self.playerGroup.sprite.speed=0
            for tiles in self.tiles:
                tiles.rect.x+=PlayerSpeed
            for tiles in self.treeAndObjectGroup:
                tiles.rect.x+=PlayerSpeed
            for tiles in self.subTiles:
                tiles.rect.x+=PlayerSpeed
            for tiles in self.borderGroup:
                tiles.rect.x+=PlayerSpeed
            for tiles in self.fightBorder:
                tiles.rect.x+=PlayerSpeed
            for tiles in self.enemyGroup:
                tiles.rect.x+=PlayerSpeed
            for tiles in self.lightGroup:
                tiles.rect.x+=PlayerSpeed
            for tiles in self.coinGroup:
                tiles.rect.x+=PlayerSpeed
            for tiles in self.checkpoints:
                tiles.rect.x+=PlayerSpeed
            for tiles in self.heartGroup:
                tiles.rect.x+=PlayerSpeed
            for tiles in self.portalGroup:
                tiles.rect.x+=PlayerSpeed
            for tiles in self.kunaiGroup:
                tiles.rect.x+=PlayerSpeed
        elif self.playerGroup.sprite.rect.x >WindowWidth*(3/4) and self.playerGroup.sprite.direction.x>0:
            self.x-=PlayerSpeed
            self.playerGroup.sprite.speed = 0
            for tiles in self.tiles:
                tiles.rect.x -= PlayerSpeed
            for tiles in self.treeAndObjectGroup:
                tiles.rect.x-=PlayerSpeed
            for tiles in self.subTiles:
                tiles.rect.x-=PlayerSpeed
            for tiles in self.borderGroup:
                tiles.rect.x-=PlayerSpeed
            for tiles in self.fightBorder:
                tiles.rect.x-=PlayerSpeed
            for tiles in self.enemyGroup:
                tiles.rect.x-=PlayerSpeed
            for tiles in self.lightGroup:
                tiles.rect.x-=PlayerSpeed
            for tiles in self.coinGroup:
                tiles.rect.x-=PlayerSpeed
            for tiles in self.checkpoints:
                tiles.rect.x-=PlayerSpeed
            for tiles in self.heartGroup:
                tiles.rect.x-=PlayerSpeed
            for tiles in self.portalGroup:
                tiles.rect.x-=PlayerSpeed
            for tiles in self.kunaiGroup:
                tiles.rect.x-=PlayerSpeed
        else:
            self.playerGroup.sprite.speed=PlayerSpeed
    def setCheckPoint(self):
        player=self.playerGroup.sprite
        minCheck = self.checkpoints.sprites()[0]
        min = abs(player.rect.x - minCheck.rect.x)
        for checkpoint in self.checkpoints.sprites():
            if abs(player.rect.x - checkpoint.rect.x) < min:
                min = abs(player.rect.x - checkpoint.rect.x)
                minCheck = checkpoint

        if (minCheck.rect.x-self.x)!=self.lastCheckPoint[0] and (minCheck.rect.x-self.x)>self.lastCheckPoint[0] and (minCheck.rect.x-self.x)<=self.playerGroup.sprite.rect.x-self.x :
            self.lastCheckPoint=[minCheck.rect.x-self.x,minCheck.rect.y]
            self.save()
    def save(self):
        with  open("save.txt", "w") as SaveFile:
            # level , last checkpoint ,score,kunai number,health
            SaveFile.write(f"{self.currentLevel}")
            SaveFile.write("\n")
            SaveFile.write(f"{self.lastCheckPoint[0]},{self.lastCheckPoint[1]}")
            SaveFile.write("\n")
            SaveFile.write(f"{self.playerGroup.sprite.score}")
            SaveFile.write("\n")
            SaveFile.write(f"{self.playerGroup.sprite.kunaiNumber}")
            SaveFile.write("\n")
            SaveFile.write(f"{self.playerGroup.sprite.health}\n")
            if OptionMenu.PlayMusic:
                SaveFile.write("1")
            else:
                SaveFile.write("0")

    def fallingFromScreen(self,player):
        if player.rect.top > WindowHeight:
            player.health -= 50
            if player.health<0:
                player.health=0
            player.die()  # checks dead
            self.playerGroup.sprite.rect.topleft = (self.lastCheckPoint[0]+self.x,self.lastCheckPoint[1]-80)
            self.scrollToPlayer(-(self.playerGroup.sprite.rect.x-500))
    def checkGameOver(self):
        if self.playerGroup.sprite.health<=0:
            self.pause[5]=1
            self.playerGroup.sprite.state="dead"
    def scrollToPlayer(self, x):
        self.x+=x
        for tiles in self.tiles:
            tiles.rect.x += x
        for tiles in self.treeAndObjectGroup:
            tiles.rect.x += x
        for tiles in self.subTiles:
            tiles.rect.x += x
        for tiles in self.borderGroup:
            tiles.rect.x += x
        for tiles in self.fightBorder:
            tiles.rect.x += x
        for tiles in self.enemyGroup:
            tiles.rect.x += x
        for tiles in self.lightGroup:
            tiles.rect.x += x
        for tiles in self.coinGroup:
            tiles.rect.x += x
        for tiles in self.checkpoints:
            tiles.rect.x += x
        for tiles in self.playerGroup:
            tiles.rect.x += x
        for tiles in self.heartGroup:
            tiles.rect.x += x
        for tiles in self.portalGroup:
            tiles.rect.x += x
        for tiles in self.kunaiGroup:
            tiles.rect.x += x
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
        if self.playerGroup.sprite.health<=0:
            self.playerGroup.sprite.health=0
        self.helthBar=pygame.surface.Surface((self.playerGroup.sprite.health*2,16))
        self.helthBar.fill((152,142,24))
        self.scoreText = self.font.render(f"Score: {self.playerGroup.sprite.score}", True, ((40, 54, 67)))
        self.kunaiText = self.font.render(f": {self.playerGroup.sprite.kunaiNumber}", True, (40, 54, 67))
    def enemyShowHealth(self):
        for enemy in self.enemyGroup.sprites():
            enemy.showHealth(self.display)
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
    def playMusic(self):
        if OptionMenu.PlayMusic==True:
            pygame.mixer.music.load("Music/NinjaManFightVer(remixAgain1).mp3")
            pygame.mixer.music.play()