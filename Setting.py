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
PlayerIdleImages=[]
PlayerIdleImagesLeft=[]
PlayerIdleImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Idle__000.png"),(232/7,439/7)))
PlayerIdleImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Idle__001.png"),(232/7,439/7)))
PlayerIdleImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Idle__002.png"),(232/7,439/7)))
PlayerIdleImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Idle__003.png"),(232/7,439/7)))
PlayerIdleImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Idle__004.png"),(232/7,439/7)))
PlayerIdleImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Idle__005.png"),(232/7,439/7)))
PlayerIdleImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Idle__006.png"),(232/7,439/7)))
PlayerIdleImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Idle__007.png"),(232/7,439/7)))
PlayerIdleImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Idle__008.png"),(232/7,439/7)))
PlayerIdleImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Idle__009.png"),(232/7,439/7)))
for image in PlayerIdleImages:
    PlayerIdleImagesLeft.append(pygame.transform.flip(image,True,False))
PlayerRunImages=[]
PlayerRunImagesLeft=[]
PlayerRunImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Run__000.png"),(363/7,439/7)))
PlayerRunImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Run__001.png"),(363/7,439/7)))
PlayerRunImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Run__002.png"),(363/7,439/7)))
PlayerRunImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Run__003.png"),(363/7,439/7)))
PlayerRunImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Run__004.png"),(363/7,439/7)))
PlayerRunImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Run__005.png"),(363/7,439/7)))
PlayerRunImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Run__006.png"),(363/7,439/7)))
PlayerRunImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Run__007.png"),(363/7,439/7)))
PlayerRunImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Run__008.png"),(363/7,439/7)))
PlayerRunImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Run__009.png"),(363/7,439/7)))
PlayerJumpImages=[]
PlayerJumpImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Jump__000.png"),(363/7,439/7)))
PlayerJumpImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Jump__001.png"),(363/7,439/7)))
PlayerJumpImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Jump__002.png"),(363/7,439/7)))
PlayerJumpImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Jump__003.png"),(363/7,439/7)))
PlayerJumpImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Jump__004.png"),(363/7,439/7)))
PlayerJumpImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Jump__005.png"),(363/7,439/7)))
PlayerJumpImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Jump__006.png"),(363/7,439/7)))
PlayerJumpImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Jump__007.png"),(363/7,439/7)))
PlayerJumpImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Jump__008.png"),(363/7,439/7)))
PlayerJumpImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Jump__009.png"),(363/7,439/7)))
PlayerJumpImagesLeft=[]
for images in PlayerJumpImages:
    PlayerJumpImagesLeft.append(pygame.transform.flip(images,True,False))
for images in PlayerRunImages:
    PlayerRunImagesLeft.append(pygame.transform.flip(images,True,False))
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

