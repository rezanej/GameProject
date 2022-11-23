import pygame
from Setting import *
from Kunai import *

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,tileGroup,kunaiGroup=pygame.sprite.Group(),bordergroup=pygame.sprite.Group(),\
                 enemyGroup=pygame.sprite.Group(),coinGroup=pygame.sprite.Group(),fightBorder=pygame.sprite.Group(),\
                 checkpoints=pygame.sprite.Group(),heartGroup=pygame.sprite.Group):
        super().__init__()
        self.image=PlayerImage
        self.rect=self.image.get_rect(topleft=(x,y))
        self.direction=pygame.math.Vector2()
        self.tileGroup=tileGroup
        self.kunaiGroup=kunaiGroup
        self.borderGroup=bordergroup
        self.enemyGroup=enemyGroup
        self.coinGroup=coinGroup
        self.fightBorder=fightBorder
        self.checkpoints=checkpoints
        self.heartGroup=heartGroup
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
        self.attackAdeadOffset=True
        self.freeRun=self.checkFreeRun()
        self.animationSpeed=PlayerAnimationSpeed
        self.health=100
        self.score=0
        self.dead=False
        self.reduceHelathCollistion=0
        self.reduceEnemyHelathCollistion=0
        self.fightBorderWork=False
        self.scrollState=True
    def setDirection(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_f] and self.kunaiNumber>0 and self.kunaiTimer==KunaiTimer:
            self.kunaiGroup.add(Kunai(self.rect.centerx,self.rect.centery,self,self.enemyGroup,KunaiSpeed))
            self.kunaiNumber-=1
            self.kunaiTimer=0
            self.state="throw"
            self.throw=True
            self.speed=0
            self.currentimageNum=0

        else :

            if keys[pygame.K_LEFT] and self.state!="throw":
                self.direction.x=-1
                self.state="run"
                self.left=True
            elif keys[pygame.K_RIGHT] and self.state!="throw":
                self.direction.x=1
                self.state="run"
                self.left = False
            elif self.state=="throw":
                if self.currentimageNum==0:
                    self.direction.x=0
                    self.state="idle"
            else :
                self.direction.x = 0
                self.state = "idle"

            if keys[pygame.K_SPACE] and self.onGround:
                self.jump()
                self.state="jump"
            if keys[pygame.K_g]:
                self.state="attack"
                self.speed=0

    def update(self,tiles):
        self.tileGroup=tiles
        if not self.dead:
            self.setDirection()
        self.onGround=False
        self.horizontalMovement()
        self.horizontalCollision()
        self.gravityFun()
        self.verticalCollision()
        self.coinCollision()
        self.heartCollision()
        self.checkJump()
        if self.freeRun:
            if self.state!="jump":
                self.state="run"
            self.direction.x=1
        self.animate()
        self.kunaiTiming()
        self.attackLeftoffset()
        self.deadLeftOffset()
    def horizontalMovement(self):
        if self.state!="throw": # for not moving during throw
            self.rect.x += self.direction.x * self.speed

    def horizontalCollision(self):
        for sprite in self.tileGroup.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.freeRun:
                    self.health-=20
                    self.rect.y-=120
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
        if self.fightBorderWork:
            for sprite in self.fightBorder.sprites():
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x>0:
                        self.rect.right=sprite.rect.left
                    if self.direction.x<0:
                        self.rect.left=sprite.rect.right
        for sprite in self.enemyGroup.sprites():
            if sprite.dead == False and self.dead==False:
                if sprite.rect.colliderect(self.rect):
                    if self.state!="attack":

                        if self.reduceHelathCollistion == 0:
                            if self.health >=10:
                                self.health -= 20
                                self.die()
                                self.reduceHelathCollistion = 20
                            else:
                                self.die()
                        elif self.reduceHelathCollistion > 0:
                            self.reduceHelathCollistion -= 1

                        if self.direction.x > 0:
                            self.rect.right = sprite.rect.left
                        if self.direction.x < 0:
                            self.rect.left = sprite.rect.right
                    else:
                        if self.reduceEnemyHelathCollistion == 0:
                            if sprite.health >20:
                                sprite.health -= 20
                                self.reduceEnemyHelathCollistion = 20
                            else:
                                pass
                                sprite.dead = True
                                sprite.currentImageNum = 0
                        elif self.reduceEnemyHelathCollistion > 0:
                            self.reduceEnemyHelathCollistion -= 1


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
        if self.fightBorderWork:
            for sprite in self.fightBorder.sprites():
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                        self.direction.y = 0
                        self.onGround=True
                    elif self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom
                        self.direction.y = 0
        for sprite in self.enemyGroup.sprites():
            if sprite.dead==False and self.dead==False:
                if sprite.rect.colliderect(self.rect):
                    if self.reduceEnemyHelathCollistion==0:
                        if sprite.health>20:
                            sprite.health-=20
                            self.die()
                            self.reduceEnemyHelathCollistion=20
                        else:
                            pass
                            sprite.dead=True
                            sprite.currentImageNum=0
                    elif self.reduceEnemyHelathCollistion>0:
                        self.reduceEnemyHelathCollistion-=1

                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                        self.direction.y = 0
                        self.onGround=True
                    elif self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom
                        self.direction.y = 0

    def coinCollision(self):
        if not self.dead:
            pygame.sprite.spritecollide(self,self.coinGroup,True)
    def heartCollision(self):
        if not self.dead:
            pygame.sprite.spritecollide(self,self.heartGroup,True)

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
                self.image=PlayerIdleImages[int(self.currentimageNum)]
            elif self.left:
                self.image = PlayerIdleImagesLeft[int(self.currentimageNum)]
            self.currentimageNum += self.animationSpeed
            if self.currentimageNum>=10:
                self.currentimageNum=0
        if self.state=="run":
            if self.direction.x > 0:
                self.left=False
                self.image=PlayerRunImages[int(self.currentimageNum)]
            if self.direction.x < 0:
                self.left = True
                self.image=PlayerRunImagesLeft[int(self.currentimageNum)]
            self.currentimageNum += self.animationSpeed
            if self.currentimageNum>=10:
                self.currentimageNum=0
        if self.state=="jump":
            if not self.left:
                self.image=PlayerJumpImages[int(self.currentimageNum)]
                self.currentimageNum+=self.animationSpeed
            else:
                self.image=PlayerJumpImagesLeft[int(self.currentimageNum)]
                self.currentimageNum += self.animationSpeed
            if self.currentimageNum>=10:
                self.currentimageNum=0
        if self.state=="attack":

            if self.left:

               self.image=PlayerAttackImagesLeft[int(self.currentimageNum)]

               self.currentimageNum+=self.animationSpeed
            else:
                self.image=PlayerAttackImages[int(self.currentimageNum)]
                self.currentimageNum+=self.animationSpeed
            if self.currentimageNum>=10:
                self.currentimageNum=0
        if self.state=="throw":
            if self.left:
               self.image=PlayerThrowImagesLeft[int(self.currentimageNum)]
               self.currentimageNum+=self.animationSpeed
            else:
                self.image=PlayerThrowImages[int(self.currentimageNum)]
                self.currentimageNum+=self.animationSpeed
            if self.currentimageNum>=10:
                self.throw=False
                self.currentimageNum=0
        if self.state=="dead":
            self.direction.x=0
            if self.dead and self.currentimageNum>=9:
                self.currentimageNum=9
            else:

                if self.left:
                   self.image=PlayerDeadImagesLeft[int(self.currentimageNum)]
                   self.currentimageNum+=self.animationSpeed
                else:
                    self.image=PlayerDeadImages[int(self.currentimageNum)]
                    self.currentimageNum+=self.animationSpeed

    def kunaiTiming(self):
        if self.kunaiTimer<KunaiTimer:
            self.kunaiTimer+=1

    def attackLeftoffset(self):
        if self.state == "attack" and self.left and self.attackAdeadOffset:

            self.rect.left -= 40
            self.attackAdeadOffset = False
        elif self.left and not self.attackAdeadOffset and self.state != "attack":
            self.attackAdeadOffset = True
            self.rect.left += 40
    def deadLeftOffset(self):
        if self.state == "dead" and self.left and self.attackAdeadOffset:

            self.rect.left -= 40
            self.attackAdeadOffset = False
        elif self.left and not self.attackAdeadOffset and self.state != "dead":
            self.attackAdeadOffset = True
            self.rect.left += 40
    def checkFreeRun(self):
        if len(self.borderGroup.sprites())==0:
            return True
        return False

    def die(self):
        if self.health<=0 and not self.dead:
            self.state="dead"
            self.dead=True
            self.currentimageNum=0

