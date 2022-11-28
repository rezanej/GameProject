import pygame
from Setting import *
import random
class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y,speed,tileGroup,playerGroup,fightBorderGroup,idleAnim,runAnim,deadAnim,idleAnimL,runAnimL,deadAnimL):
        super().__init__()
        self.idleAnim=idleAnim
        self.runAnim=runAnim
        self.deadAnim=deadAnim
        self.idleAnimL=idleAnimL
        self.runAnimL=runAnimL
        self.deadAnimL=deadAnimL
        self.image = self.idleAnim[0]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.direction = pygame.math.Vector2()
        self.tileGroup = tileGroup
        self.speed = 0
        self.speedTemp=speed
        self.gravity = Gravity
        self.state = "idle"
        self.currentimageNum = 0
        self.left = False
        self.movementLength=2*40
        self.direction.x=1
        self.animationSpeed=0.4
        self.health=100
        self.dead=False
        self.seenPlayer=True
        self.playerGroup=playerGroup
        self.fightBorderGroup=fightBorderGroup
        self.idleTimer=60
        self.borderTimer=0
        self.once=False
        self.once1=True
        self.rect.height -= 5
    def chekcIdle(self):
        if self.once1:
            if self.idleTimer>0:
                self.idleTimer-=1
            elif self.idleTimer==0 and self.once:
                self.state="idle"
                self.idleTimer=random.randint(30,100)
                self.speed = 0
                self.once=False
            elif self.idleTimer==0 and not self.once:
                self.state = "run"
                self.idleTimer = random.randint(30,100)
                self.speed =self.speedTemp
                self.once = True
        else:
            self.state = "run"
            self.speed = self.speedTemp
    def setDirection(self):
        b=self.seenPlayerF()
        if self.borderTimer>0:
            self.seenPlayer=False
            self.borderTimer-=1
        if not self.seenPlayer:
            if self.state=="run":
                self.movementLength-=1
            if self.movementLength==0:
                self.direction.x*=-1
                self.movementLength=2*40
                self.left= not self.left
        elif self.playerGroup.sprite.dead!=True:
            self.once1=False
            self.playerGroup.sprite.fightBorderWork=True
            self.direction.x=b

    def horizontalCollision(self):
        for sprite in self.tileGroup.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right
        for sprite in self.fightBorderGroup.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left
                    self.direction.x *= -1
                    self.borderTimer=10
                elif self.direction.x < 0:
                    self.rect.left = sprite.rect.right
                    self.direction.x *= -1
                    self.borderTimer=10

    def seenPlayerF(self):

        if abs(self.rect.x - self.playerGroup.sprite.rect.x) < 200 and abs(self.rect.x - self.playerGroup.sprite.rect.x) > 50 and self.rect.x - self.playerGroup.sprite.rect.x <0:
            self.seenPlayer=True
            return 1
        elif abs(self.rect.x - self.playerGroup.sprite.rect.x) < 200 and abs(self.rect.x - self.playerGroup.sprite.rect.x) > 50 and self.rect.x -self.playerGroup.sprite.rect.x > 0:
            self.seenPlayer=True
            return -1
        else :
            self.seenPlayer=False
            return 0
    def verticalCollision(self):
        for sprite in self.tileGroup.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.onGround = True
                elif self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0

    def gravityFun(self):
        self.direction.y += self.gravity
        self.rect.centery += self.direction.y

    def animate(self):
        if self.state=="idle":
            if self.currentimageNum>=len(self.idleAnim)-2:
                self.currentimageNum=0
            if not self.left:
                self.image=self.idleAnim[int(self.currentimageNum)]
            elif self.left:
                self.image =self.idleAnimL[int(self.currentimageNum)]
            self.currentimageNum += self.animationSpeed
        if self.state=="run":
            if self.currentimageNum>=len(self.runAnim)-2:
                self.currentimageNum=0
            if self.direction.x > 0:
                self.left=False
                self.image=self.runAnim[int(self.currentimageNum)]
            if self.direction.x < 0:
                self.left = True
                self.image=self.runAnimL[int(self.currentimageNum)]
            self.currentimageNum += self.animationSpeed

    def horizontalMovement(self):
        self.rect.x += self.direction.x * self.speed

    def showHealth(self,display):
        if not self.dead:
            self.helthBar = pygame.surface.Surface((self.health/2, 8))
            self.helthBar.fill((0, 156, 56))
            self.helthBarRect = self.helthBar.get_rect(topleft=(self.rect.centerx-24,self.rect.centery-34))
            self.helthBarBackground = pygame.rect.Rect(self.rect.left+15,self.rect.top-2, 50, 8)
            display.blit(self.helthBar,self.helthBarRect)
            pygame.draw.rect(display,(255,0,0),self.helthBarBackground,2)
    def update(self):
        if not self.dead:
            self.chekcIdle()
            self.setDirection()
            self.horizontalMovement()
            self.horizontalCollision()
            self.gravityFun()
            self.verticalCollision()
            self.animate()
        else:
            self.die()
    def die(self):
        if self.dead and not self.currentimageNum>=len(self.deadAnim)-1:
            self.playerGroup.sprite.fightBorderWork = False
            if not self.left:
                self.image = self.deadAnim[int(self.currentimageNum)]
            elif self.left:
                self.image = self.deadAnimL[int(self.currentimageNum)]
            self.currentimageNum += self.animationSpeed
