import pygame
WindowWidth=64*20 #temporary
WindowHeight=64*10 #temporary
Fps=60
CurrentLevel=0
PlayerSpeed=8
PlayerJumpSpeed=15
Gravity=3
BackgroundImages=[]
Grassimages=[]
Grassimages.append(pygame.transform.scale(pygame.image.load("Level1Assets/Tiles/2.png"),(64,64)))
BackgroundImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/BG/BG.png"),(64*20,640)))
PlayerImage=pygame.transform.scale(pygame.image.load("PlayerImages/Idle__000.png"),(232/7,439/7))
Level1TileMap="00000000000000000000n" \
              "00000000000000000000n" \
              "0p000000000000000000n" \
              "11110000110000011000n" \
              "00000000000000000000n" \
              "00011111110000000000n" \
              "00000000000000000000n" \
              "00000000000000000000n" \
              "00000000000000000000n" \
              "00000000000000000000n"

