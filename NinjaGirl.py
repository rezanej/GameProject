import pygame
import Enemy
from Kunai import Kunai
from Setting import  *
class NinjaGirl(Enemy.Enemy):
    def __init__(self,x,y,speed,tileGroup,playerGroup,fightBorderGroup,idleAnim,runAnim,deadAnim,\
                 idleAnimL,runAnimL,deadAnimL,throwAnim,throwAnimL,kunaiGroup):
        super().__init__(x,y,speed,tileGroup,playerGroup,fightBorderGroup,idleAnim,\
                         runAnim,deadAnim,idleAnimL,runAnimL,deadAnimL)
        self.throwAnim=throwAnim
        self.throwAnimL=throwAnimL
        self.throw = False
        self.throwTimer=70
        self.health=200
        self.kunaiGroup=kunaiGroup
        self.once=True
    def animate(self):
        super().animate()
        if self.state=="throw":
            if self.left:
               self.image= self.throwAnimL[int(self.currentimageNum)]
               self.currentimageNum+=self.animationSpeed
            else:
                self.image= self.throwAnim[int(self.currentimageNum)]
                self.currentimageNum+=self.animationSpeed
            if self.currentimageNum>=10:
                self.throw=False
                self.currentimageNum=0
    def setDirection(self):
        super().setDirection()

    def seenPlayerF(self):
        if abs(self.rect.x - self.playerGroup.sprite.rect.x) < 300 and abs(self.rect.x - self.playerGroup.sprite.rect.x) > 20 and self.rect.x - self.playerGroup.sprite.rect.x <0:
            self.throw=True
            self.throwCheck()
            self.seenPlayer=True
            return 1
        elif abs(self.rect.x - self.playerGroup.sprite.rect.x) < 300 and abs(self.rect.x - self.playerGroup.sprite.rect.x) > 20 and self.rect.x -self.playerGroup.sprite.rect.x > 0:
            self.throw=True
            self.throwCheck()
            self.seenPlayer = True
            return -1
        else :self.throw=False
        super().seenPlayerF()
    def throwCheck(self):
        if self.throwTimer<70:
            self.throwTimer+=1
        if self.throwTimer==70 and self.throw:
            self.throwF()
    def throwF(self):
        self.kunaiGroup.add(Kunai(self.rect.centerx, self.rect.centery, self, self.playerGroup,KunaiSpeed//2))
        self.throwTimer = 0
    def showHealth(self,display):
        if not self.dead:
            self.helthBar = pygame.surface.Surface((self.health/4, 8))
            self.helthBar.fill((0, 156, 56))
            self.helthBarRect = self.helthBar.get_rect(topleft=(self.rect.centerx-14,self.rect.centery-34))
            self.helthBarBackground = pygame.rect.Rect(self.rect.left+6,self.rect.top, 50, 8)
            display.blit(self.helthBar,self.helthBarRect)
            pygame.draw.rect(display,(255,0,0),self.helthBarBackground,2)
    def die(self):
        super().die()
        if self.once:
            self.playerGroup.sprite.kunaiNumber+=2
            self.once=False