import pygame
from Setting import *
import Ice
class IceSpell(pygame.sprite.Sprite):
    def __init__(self,x,y,player,enemies,speed,collectable=False,iceGroup=pygame.sprite.Group()):
        super().__init__()
        self.lifeTime=KunaiLifetime
        if player.left:
            self.direction=-1
        else:
            self.direction=1
        self.image=IceSpellImage
        self.collectable=collectable
        self.rect = self.image.get_rect(center=(x, y))
        self.player=player
        self.speed=speed
        self.enemies=enemies
        self.lifeTime = KunaiLifetime*self.speed
        self.iceGroup=iceGroup
        self.colidedSprite=0
    def update(self):
        if self.collectable:
            self.collectCollition()
        else:
            self.move()
            self.life()
            self.collition()
    def move(self):
        if self.direction>0:
            self.rect.x+=self.speed
        elif self.direction<0:
            self.rect.x-=self.speed
    def life(self):
        self.lifeTime -= 1
        if self.lifeTime < 0:
            self.kill()
            if self.colidedSprite!=0:
                self.colidedSprite.freeze=False
                self.colidedSprite.freezeOnce=False
    def collition(self):
        for sprite in self.enemies:
            if self.rect.colliderect(sprite):
                sprite.health-=20
                sprite.freeze=True
                self.colidedSprite=sprite
                self.iceGroup.add(Ice.Ice(sprite.rect.x,sprite.rect.y,FreezeIceImages,sprite))
                if sprite.health<=0:
                    sprite.dead=True
                self.kill()

    def collectCollition(self):
        if self.rect.colliderect(self.player.rect):
            self.player.iceSpellNumber+=1
            self.kill()
