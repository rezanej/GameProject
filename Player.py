import pygame
from Setting import *
from Kunai import *

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,tileGroup,kunaiGroup=pygame.sprite.Group(),bordergroup=pygame.sprite.Group()):
        super().__init__()
        self.image=PlayerImage
        self.rect=self.image.get_rect(topleft=(x,y))
        self.direction=pygame.math.Vector2()
        self.tileGroup=tileGroup
        self.kunaiGroup=kunaiGroup
        self.borderGroup=bordergroup
        self.jumpSpeed=PlayerJumpSpeed
        self.speed=PlayerSpeed
        self.gravity=Gravity
        self.state="idle"
        self.throw=False
        self.currentimageNum=0
        self.kunaiNumber=StartKunai
        self.kunaiTimer=KunaiTimer
        self.left=False
        self.onGround=False
        self.attckOffset=True
        self.freeRun=self.checkFreeRun()
    def setDirection(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_f] and self.kunaiNumber>0 and self.kunaiTimer==KunaiTimer:
            self.kunaiGroup.add(Kunai(self.rect.centerx,self.rect.centery,self))
            self.kunaiNumber-=1
            self.kunaiTimer=0
            self.state="throw"
            self.throw=True
            self.speed=0
            self.currentimageNum=0

        else :
            if keys[pygame.K_LEFT]:
                self.direction.x=-1
                self.state="run"
                self.left=True
            elif keys[pygame.K_RIGHT]:
                self.direction.x=1
                self.state="run"
                self.left = False
            else:
                self.direction.x=0
                self.state="idle"

            if keys[pygame.K_SPACE] and self.onGround:
                self.jump()
                self.state="jump"
            if keys[pygame.K_g]:
                self.state="attack"
                self.speed=0



    def update(self,tiles):
        self.tileGroup=tiles
        self.setDirection()
        self.onGround=False
        self.horizontalMovement()
        self.horizontalCollision()
        self.gravityFun()
        self.verticalCollision()
        self.checkJump()
        if self.freeRun:
            if self.state!="jump":
                self.state="run"
            self.direction.x=1
        self.animate()
        self.kunaiTiming()
        self.attackLeftoffset()
    def horizontalMovement(self):
        self.rect.x += self.direction.x * self.speed

    def horizontalCollision(self):
        for sprite in self.tileGroup.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.x>0:
                    self.rect.right=sprite.rect.left
                if self.direction.x<0:
                    self.rect.left=sprite.rect.right
        for sprite in self.borderGroup.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.x>0:
                    self.rect.right=sprite.rect.left
                if self.direction.x<0:
                    self.rect.left=sprite.rect.right

    def verticalCollision(self):
        for sprite in self.tileGroup.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.onGround=True
                elif self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0
        for sprite in self.borderGroup.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.onGround=True
                elif self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0

    def jump(self):
        self.direction.y=-self.jumpSpeed
    def gravityFun(self):
        self.direction.y += self.gravity
        self.rect.centery += self.direction.y
    def checkJump(self):
        if self.direction.y <0:
            self.state="jump"
    # def verticalMovement(self):
    #     self.direction.y+=4
    #     self.rect.y+=self.direction.y
    def animate(self):
        if self.state=="idle":
            if not self.left:
                self.image=PlayerIdleImages[self.currentimageNum]
            elif self.left:
                self.image = PlayerIdleImagesLeft[self.currentimageNum]
            self.currentimageNum += 1
            if self.currentimageNum==10:
                self.currentimageNum=0
        if self.state=="run":
            if self.direction.x > 0:
                self.left=False
                self.image=PlayerRunImages[self.currentimageNum]
            if self.direction.x < 0:
                self.left = True
                self.image=PlayerRunImagesLeft[self.currentimageNum]
            self.currentimageNum += 1
            if self.currentimageNum==10:
                self.currentimageNum=0
        if self.state=="jump":
            if not self.left:
                self.image=PlayerJumpImages[self.currentimageNum]
                self.currentimageNum+=1
            else:
                self.image=PlayerJumpImagesLeft[self.currentimageNum]
                self.currentimageNum += 1
            if self.currentimageNum==10:
                self.currentimageNum=0
        if self.state=="attack":

            if self.left:

               self.image=PlayerAttackImagesLeft[self.currentimageNum]

               self.currentimageNum+=1
            else:
                self.image=PlayerAttackImages[self.currentimageNum]
                self.currentimageNum+=1
            if self.currentimageNum==10:
                self.currentimageNum=0
        if self.state=="throw":
            if self.left:
               self.image=PlayerThrowImagesLeft[self.currentimageNum]
               self.currentimageNum+=1
            else:
                self.image=PlayerThrowImages[self.currentimageNum]
                self.currentimageNum+=1
            if self.currentimageNum==10:
                self.throw=False
                self.currentimageNum=0
    def kunaiTiming(self):
        if self.kunaiTimer<KunaiTimer:
            self.kunaiTimer+=1

    def attackLeftoffset(self):
        if self.state == "attack" and self.left and self.attckOffset:

            self.rect.left -= 40
            self.attckOffset = False
        elif self.left and not self.attckOffset and self.state != "attack":
            self.attckOffset = True
            self.rect.left += 40
    def checkFreeRun(self):
        if len(self.borderGroup.sprites())==0:
            return True
        return False

