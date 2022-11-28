import pygame

from Kunai import Kunai
import random
from Setting import  *
from FireBall import FireBall
class Boss(pygame.sprite.Sprite):
    def __init__(self,x,y,speed,tileGroup,playerGroup,fightBorderGroup,idle0,idle0Left,idle1,idle1left,idle2,idle2left,kunaiGroup):
        super().__init__()
        self.throw = False
        self.throwTimer=150
        self.kunaiGroup=kunaiGroup
        self.idleAnim0 = idle0
        self.idleAnim0left = idle0Left
        self.idleAnim1 = idle1
        self.idleAnim1left = idle1left
        self.deadAnim = idle2
        self.deadAnimleft = idle2left
        self.image = self.idleAnim0[0]
        self.x,self.y=x,y
        self.rect = self.image.get_rect(topleft=(x, y))
        self.direction = pygame.math.Vector2()
        self.tileGroup = tileGroup
        self.speed = 0
        self.speedTemp = speed
        self.gravity = Gravity
        self.state = "idle"
        self.currentimageNum = 0
        self.left = False
        self.movementLength = 2 * 40
        self.direction.x = 1
        self.animationSpeed = 0.4
        self.health = 300
        self.dead = False
        self.seenPlayer = True
        self.playerGroup = playerGroup
        self.fightBorderGroup = fightBorderGroup
        self.idleTimer = 60
        self.borderTimer = 0
        self.once = False
        self.once1 = True
        self.rect.height -= 5
    def checkIdle(self):
        if self.once1:
            if self.idleTimer > 0:
                self.idleTimer -= 1
            elif self.idleTimer == 0 and self.once:
                self.idleTimer = random.randint(30, 100)
                self.speed = 0
                self.once = False
            elif self.idleTimer == 0 and not self.once:
                self.idleTimer = random.randint(30, 100)
                self.speed = self.speedTemp
                self.once = True
        else:
            self.speed = self.speedTemp
    def setDirection(self):
        b = self.seenPlayerF()
        if self.borderTimer > 0:
            self.seenPlayer = False
            self.borderTimer -= 1
        if not self.seenPlayer:
            if self.speed!=0:
                self.movementLength -= 1
            if self.movementLength == 0:
                self.direction.x *= -1
                self.movementLength = 2 * 40
                self.left = not self.left
        elif self.playerGroup.sprite.dead != True:
            self.once1 = False
            self.playerGroup.sprite.fightBorderWork = True
            self.direction.x = b

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
                    self.borderTimer = 10
                elif self.direction.x < 0:
                    self.rect.left = sprite.rect.right
                    self.direction.x *= -1
                    self.borderTimer = 10

    def seenPlayerF(self):
        if abs(self.rect.x - self.playerGroup.sprite.rect.x) < 600 and abs(self.rect.x - self.playerGroup.sprite.rect.x) > 20 and self.rect.x - self.playerGroup.sprite.rect.x <0:
            self.throw=True
            self.throwCheck()
            self.seenPlayer=True
            self.direction.x = 1
            self.left=False
            return 1
        elif abs(self.rect.x - self.playerGroup.sprite.rect.x) < 600 and abs(self.rect.x - self.playerGroup.sprite.rect.x) > 20 and self.rect.x -self.playerGroup.sprite.rect.x > 0:
            self.throw=True
            self.throwCheck()
            self.seenPlayer = True
            self.left=True
            return -1
        else :
            self.throw=False

            if abs(self.rect.x - self.playerGroup.sprite.rect.x) < 200 and abs(
                    self.rect.x - self.playerGroup.sprite.rect.x) > 50 and self.rect.x - self.playerGroup.sprite.rect.x < 0:
                self.seenPlayer = True
                return 1
            elif abs(self.rect.x - self.playerGroup.sprite.rect.x) < 200 and abs(
                    self.rect.x - self.playerGroup.sprite.rect.x) > 50 and self.rect.x - self.playerGroup.sprite.rect.x > 0:
                self.seenPlayer = True
                return -1
            else:
                self.seenPlayer = False
                return 0

    def throwCheck(self):
        if self.throwTimer<150:
            self.throwTimer+=1
        if self.throwTimer==150 and self.throw:
            self.throwF()
    def throwF(self):
        self.kunaiGroup.add(FireBall(self.rect.centerx, self.rect.centery+60, self, self.playerGroup,KunaiSpeed//3))
        self.throwTimer = 0
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
        if self.state == "idle":
            if self.currentimageNum >= len(self.idleAnim0) - 2:
                self.currentimageNum = 0
            if not self.left:
                self.image = self.idleAnim0[int(self.currentimageNum)]
            elif self.left:
                self.image = self.idleAnim0left[int(self.currentimageNum)]
            self.currentimageNum += self.animationSpeed

    def horizontalMovement(self):

        self.rect.x += self.direction.x * self.speed

    def showHealth(self, display):
        if not self.dead:
            self.helthBar = pygame.surface.Surface((self.health, 8))
            self.helthBar.fill((0, 156, 56))
            self.helthBarRect = self.helthBar.get_rect(topleft=(self.rect.centerx - 139, self.rect.centery - 93))
            self.helthBarBackground = pygame.rect.Rect(self.rect.left - 55, self.rect.top - 2, 300, 8)
            display.blit(self.helthBar, self.helthBarRect)
            pygame.draw.rect(display, (255, 0, 0), self.helthBarBackground, 2)

    def update(self):
        if not self.dead:
            self.checkIdle()
            self.setDirection()
            self.horizontalMovement()
            self.horizontalCollision()
            self.gravityFun()
            self.verticalCollision()
            self.animate()
        else:
            self.die()

    def die(self):
        if self.dead and not self.currentimageNum >= len(self.deadAnim) - 1:
            self.playerGroup.sprite.fightBorderWork = False
            if not self.left:
                self.image = self.deadAnim[int(self.currentimageNum)]
            elif self.left:
                self.image = self.deadAnimleft[int(self.currentimageNum)]
            self.currentimageNum += self.animationSpeed
