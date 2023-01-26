import pygame

import FireBall
from Setting import *
from Kunai import *
from IceSpell import IceSpell
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,tileGroup,kunaiGroup=pygame.sprite.Group(),bordergroup=pygame.sprite.Group(),\
                 enemyGroup=pygame.sprite.Group(),coinGroup=pygame.sprite.Group(),fightBorder=pygame.sprite.Group(),\
                 checkpoints=pygame.sprite.Group(),heartGroup=pygame.sprite.Group,iceGroup=pygame.sprite.Group):
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
        self.iceGroup=iceGroup
        self.jumpSpeed=PlayerJumpSpeed
        self.speed=PlayerSpeed
        self.gravity=Gravity
        self.state="idle"
        self.throw=False
        self.currentimageNum=0
        self.kunaiNumber=StartKunai
        self.iceSpellNumber=StartIceSpell
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
        self.rect.height -= 3
        self.attackStamina=100
        self.addStaminaTimer=300
        self.combatMode=1
        self.doubleJumpTimer=0
        self.canDoubleJump=False
    def setDirection(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_1]:
            self.combatMode=1
        elif keys[pygame.K_2]:
            self.combatMode = 2
        elif keys[pygame.K_3]:
            self.combatMode = 3

        if keys[pygame.K_f] and self.kunaiNumber>0 and self.kunaiTimer==KunaiTimer:
            if self.combatMode==1:
                self.kunaiGroup.add(Kunai(self.rect.centerx,self.rect.centery,self,self.enemyGroup,KunaiSpeed))
            elif self.combatMode==2:
                self.kunaiGroup.add(FireBall.FireBall(self.rect.centerx,self.rect.centery,self,self.enemyGroup,KunaiSpeed,BlueFireImagesLeft,BlueFireImages,1))
                self.kunaiNumber-=2 # decreasing 3 , 2 here 1 in a few lines belower
            elif self.combatMode==3:
                self.kunaiGroup.add(FireBall.FireBall(self.rect.centerx,self.rect.centery,self,self.enemyGroup,KunaiSpeed,BlueFireImagesLeft,BlueFireImages))
                self.kunaiNumber-=1 # decreacing 2 ,....
            self.kunaiNumber-=1
            self.kunaiTimer=0
            self.state="throw"
            self.throw=True
            self.speed=0
            self.direction.x=0
            self.currentimageNum=0
        elif keys[pygame.K_e] and self.iceSpellNumber>0 and self.kunaiTimer==KunaiTimer and self.combatMode==3:
            self.kunaiGroup.add(IceSpell(self.rect.centerx,self.rect.centery,self,self.enemyGroup,KunaiSpeed,iceGroup=self.iceGroup))
            self.iceSpellNumber-=1
            self.kunaiTimer=0
            self.state="throw"
            self.throw=True
            self.speed=0
            self.direction.x=0
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

            if keys[pygame.K_SPACE] and (self.onGround or (self.doubleJumpTimer>15 and self.doubleJumpTimer<20 and self.canDoubleJump) ) :
                self.jump()
                self.state="jump"
                self.doubleJumpTimer=0
                if self.onGround==False:
                    self.canDoubleJump=False
            if keys[pygame.K_g] and self.attackStamina>0:
                self.attackStamina-=1
                self.state="attack"
                self.speed=0
                self.direction.x=0
    def checkDoubleJump(self):
        if self.doubleJumpTimer<20 and not self.onGround:
            self.doubleJumpTimer+=1

    def addStamina(self):
        self.addStaminaTimer-=1
        if self.addStaminaTimer==0:
            self.attackStamina=100
            self.addStaminaTimer=300
    def update(self,tiles):
        self.tileGroup=tiles
        self.addStamina()
        self.checkDoubleJump()
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
        if self.freeRun and self.dead==False:
            if self.state!="jump":
                self.state="run"
            self.direction.x=1
        self.animate()
        self.kunaiTiming()
        self.deadLeftOffset()
        self.attackLeftoffset()
    def horizontalMovement(self):
        if self.state!="throw": # for not moving during throw
            self.rect.x += self.direction.x * self.speed

    def horizontalCollision(self):
        for sprite in self.tileGroup.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.freeRun:
                    self.health-=20
                    if self.health<=0:
                        self.die()
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
                            if self.health >=5:
                                self.health -= 5
                                self.die()
                                self.reduceHelathCollistion = 120
                            else:
                                self.die()
                        elif self.reduceHelathCollistion > 0:
                            self.reduceHelathCollistion -= 1

                        # if self.direction.x > 0:
                        #     self.rect.right = sprite.rect.left
                        # if self.direction.x < 0:
                        #     self.rect.left = sprite.rect.right
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
                    self.canDoubleJump=True
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
                        self.canDoubleJump=True
                    elif self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom
                        self.direction.y = 0
                        self.canDoubleJump = False
        for sprite in self.enemyGroup.sprites():
            if sprite.dead==False and self.dead==False:
                if sprite.rect.colliderect(self.rect):
                    if self.reduceEnemyHelathCollistion==0:
                        if sprite.health>10:
                            sprite.health-=0
                            self.die()
                            self.reduceEnemyHelathCollistion=40
                        else:
                            pass
                            sprite.dead=True
                            sprite.currentImageNum=0
                    elif self.reduceEnemyHelathCollistion>0:
                        self.reduceEnemyHelathCollistion-=1

                    # if self.direction.y > 0:
                    #     self.rect.bottom = sprite.rect.top
                    #     self.direction.y = 0
                    #     self.onGround=True
                    # elif self.direction.y < 0:
                    #     self.rect.top = sprite.rect.bottom
                    #     self.direction.y = 0

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

        if self.combatMode==1:
            pass
        elif self.combatMode==2:
            self.changeColor(0)
        elif self.combatMode==3:
            self.changeColor(220)
    def changeColor(self,hue):
        self.tempImage = self.image.copy()
        colorImage = pygame.Surface(self.image.get_size()).convert_alpha()
        color = pygame.Color(0)
        color.hsla = (hue, 100, 60, 100)
        colorImage.fill(color)
        self.tempImage.blit(colorImage, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        self.image = self.tempImage

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
            self.gravity-=0.3
            return True
        return False

    def die(self):
        if self.health<=0 and not self.dead:
            self.state="dead"
            self.dead=True
            self.currentimageNum=0

