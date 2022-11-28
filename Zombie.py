import pygame
import Enemy
from Setting import  *
class Zombie(Enemy.Enemy):
    def __init__(self,x,y,speed,tileGroup,playerGroup,fightBorderGroup,idleAnim,runAnim,deadAnim,\
                 idleAnimL,runAnimL,deadAnimL):
        super().__init__(x,y,speed,tileGroup,playerGroup,fightBorderGroup,idleAnim,\
                         runAnim,deadAnim,idleAnimL,runAnimL,deadAnimL)
        self.health=150

    def gravityFun(self):
        self.direction.y += self.gravity
        self.rect.centery += self.direction.y
    def showHealth(self,display):
        if not self.dead:
            self.helthBar = pygame.surface.Surface(((self.health)/3, 8))
            self.helthBar.fill((0, 156, 56))
            self.helthBarRect = self.helthBar.get_rect(topleft=(self.rect.centerx-25,self.rect.centery-35))
            self.helthBarBackground = pygame.rect.Rect(self.rect.left+5,self.rect.top, 50, 8)
            display.blit(self.helthBar,self.helthBarRect)
            pygame.draw.rect(display,(255,0,0),self.helthBarBackground,2)
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
