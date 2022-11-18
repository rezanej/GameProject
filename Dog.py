import pygame
from Setting import *

class Dog(pygame.sprite.Sprite):
    def __init__(self,x,y,tileGroup):
        super().__init__()
        self.image = DogIdleImages[0]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.direction = pygame.math.Vector2()
        self.tileGroup = tileGroup
        self.speed = DogSpeed
        self.gravity = Gravity
        self.state = "run"
        self.currentimageNum = 0
        self.left = False
        self.movementLength=2*40
        self.direction.x=1
        self.animationSpeed=0.4
    def setDirection(self):
        self.movementLength-=1
        if self.movementLength==0:
            self.direction.x*=-1
            self.movementLength=2*40
            self.left= not self.left
    def horizontalCollision(self):
        for sprite in self.tileGroup.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right


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

                elif self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0

    def gravityFun(self):
        self.direction.y += self.gravity
        self.rect.centery += self.direction.y

    def animate(self):
        if self.state=="idle":
            if not self.left:
                self.image=DogIdleImages[int(self.currentimageNum)]
            elif self.left:
                self.image = DogIdleImagesLeft[int(self.currentimageNum)]
            self.currentimageNum += self.animationSpeed
            if self.currentimageNum>=10:
                self.currentimageNum=0
        if self.state=="run":
            if self.direction.x > 0:
                self.left=False

                self.image=DogRunImages[int(self.currentimageNum)]
            if self.direction.x < 0:
                self.left = True
                self.image=DogRunImagesLeft[int(self.currentimageNum)]
            self.currentimageNum += self.animationSpeed
            if self.currentimageNum>=8:
                self.currentimageNum=0
    def horizontalMovement(self):
        self.rect.x += self.direction.x * self.speed


    def update(self):
        self.setDirection()
        self.horizontalMovement()
        self.horizontalCollision()
        self.gravityFun()
        self.verticalCollision()
        self.animate()