import pygame

class Light(pygame.sprite.Sprite):
    #1,2,3 for hardness
    def __init__(self,x,y,hardness):
        print("dfd")
        super().__init__()
        if hardness==1:
            self.image = pygame.image.load("light_350_med.png").convert_alpha()
            self.rect = self.image.get_rect(center=(x,y))
            self.image.fill((255, 255, 255, 120), None, pygame.BLEND_RGBA_MULT)