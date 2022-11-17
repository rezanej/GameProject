import pygame
WindowWidth=64*20 #temporary
WindowHeight=64*10 #temporary
Fps=60
CurrentLevel=0
PlayerSpeed=8
PlayerJumpSpeed=35
Gravity=3
KunaiSpeed=50
StartKunai=40
KunaiLifetime=15
KunaiTimer=20
BackgroundImages=[]
Grassimages=[]
Grassimages.append(pygame.transform.scale(pygame.image.load("Level1Assets/Tiles/2.png"),(64,64)))
BackgroundImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/BG/BG.png"),(64*20,640)))
PlayerImage=pygame.transform.scale(pygame.image.load("PlayerImages/Idle__000.png"),(232/7,439/7))
DirtImages=[]
DirtImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/Tiles/5.png"),(64,64)))
DirtImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/Tiles/8.png"),(64,64)))
WaterImages=[]
WaterImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/Tiles/17.png"),(64,64)))
WaterImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/Tiles/18.png"),(64,64)))
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

PlayerAttackImages=[]
PlayerAttackImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Attack__000.png"),(538/7,495/7)))
PlayerAttackImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Attack__001.png"),(538/7,495/7)))
PlayerAttackImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Attack__002.png"),(538/7,495/7)))
PlayerAttackImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Attack__003.png"),(538/7,495/7)))
PlayerAttackImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Attack__004.png"),(538/7,495/7)))
PlayerAttackImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Attack__005.png"),(538/7,495/7)))
PlayerAttackImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Attack__006.png"),(538/7,495/7)))
PlayerAttackImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Attack__007.png"),(538/7,495/7)))
PlayerAttackImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Attack__008.png"),(538/7,495/7)))
PlayerAttackImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Attack__009.png"),(538/7,495/7)))
PlayerAttackImagesLeft=[]
for image in PlayerAttackImages:
    PlayerAttackImagesLeft.append(pygame.transform.flip(image,True,False))

PlayerThrowImages=[]
PlayerThrowImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Throw__000.png"),(377/7,451/7)))
PlayerThrowImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Throw__001.png"),(377/7,451/7)))
PlayerThrowImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Throw__002.png"),(377/7,451/7)))
PlayerThrowImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Throw__003.png"),(377/7,451/7)))
PlayerThrowImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Throw__004.png"),(377/7,451/7)))
PlayerThrowImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Throw__005.png"),(377/7,451/7)))
PlayerThrowImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Throw__006.png"),(377/7,451/7)))
PlayerThrowImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Throw__007.png"),(377/7,451/7)))
PlayerThrowImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Throw__008.png"),(377/7,451/7)))
PlayerThrowImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Throw__009.png"),(377/7,451/7)))
PlayerThrowImagesLeft=[]
for image in PlayerThrowImages:
    PlayerThrowImagesLeft.append(pygame.transform.flip(image,True,False))

KunaiImgae=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("PlayerImages/Kunai.png"),(32/4,160/4)),90)
KunaiImgae=pygame.transform.flip(KunaiImgae,True,False)
KunaiImgaeLeft=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("PlayerImages/Kunai.png"),(32/4,160/4)),90)


TreeImages=[]
TreeImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/Object/Tree_1.png"),(116/2,44/2)))
TreeImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/Object/Tree_2.png"),(282/2,301/2)))

Level1TileMap="00000000000000000000000000000000000000000000000000n" \
              "00000000000000000000000000000000000000000000000000n" \
              "00000000000000000000000000000000000000000000000000n" \
              "b0000b00000000000000000000000000000000000000000000n" \
              "b0000b00000000000000000000000000000000000000000000n" \
              "b0T00b00T000000p00000000000TT00000000000000000000n" \
              "11111111110000011001100000111100000000000000000000n" \
              "dddddddd0000T00000000010t01000010t0010000000000000n" \
              "dddddddd111111wwwwwwwww11wwwwwww111wwwwwwwwwwwwwwwn" \
              "ddddddddddddddWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWn"

