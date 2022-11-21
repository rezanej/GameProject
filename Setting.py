import pygame
pygame.init()
WindowWidth=64*20 #temporary
WindowHeight=64*10 #temporary
Fps=60
CurrentLevel=0
PlayerSpeed=8
DogSpeed=3
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

DogIdleImages=[]

DogIdleImages.append(pygame.transform.scale(pygame.image.load("dog/Idle (1).png"),(547/7,481/7)))
DogIdleImages.append(pygame.transform.scale(pygame.image.load("dog/Idle (2).png"),(547/7,481/7)))
DogIdleImages.append(pygame.transform.scale(pygame.image.load("dog/Idle (3).png"),(547/7,481/7)))
DogIdleImages.append(pygame.transform.scale(pygame.image.load("dog/Idle (4).png"),(547/7,481/7)))
DogIdleImages.append(pygame.transform.scale(pygame.image.load("dog/Idle (5).png"),(547/7,481/7)))
DogIdleImages.append(pygame.transform.scale(pygame.image.load("dog/Idle (6).png"),(547/7,481/7)))
DogIdleImages.append(pygame.transform.scale(pygame.image.load("dog/Idle (7).png"),(547/7,481/7)))
DogIdleImages.append(pygame.transform.scale(pygame.image.load("dog/Idle (8).png"),(547/7,481/7)))
DogIdleImages.append(pygame.transform.scale(pygame.image.load("dog/Idle (9).png"),(547/7,481/7)))
DogIdleImages.append(pygame.transform.scale(pygame.image.load("dog/Idle (10).png"),(547/7,481/7)))
DogIdleImagesLeft=[]
for image in DogIdleImages:
    DogIdleImagesLeft.append(pygame.transform.flip(image,True,False))

DogRunImages=[]
DogRunImages.append(pygame.transform.scale(pygame.image.load("dog/Run (1).png"),(547/7,481/7)))
DogRunImages.append(pygame.transform.scale(pygame.image.load("dog/Run (2).png"),(547/7,481/7)))
DogRunImages.append(pygame.transform.scale(pygame.image.load("dog/Run (3).png"),(547/7,481/7)))
DogRunImages.append(pygame.transform.scale(pygame.image.load("dog/Run (4).png"),(547/7,481/7)))
DogRunImages.append(pygame.transform.scale(pygame.image.load("dog/Run (5).png"),(547/7,481/7)))
DogRunImages.append(pygame.transform.scale(pygame.image.load("dog/Run (6).png"),(547/7,481/7)))
DogRunImages.append(pygame.transform.scale(pygame.image.load("dog/Run (7).png"),(547/7,481/7)))
DogRunImages.append(pygame.transform.scale(pygame.image.load("dog/Run (8).png"),(547/7,481/7)))
DogRunImagesLeft=[]
for image in DogRunImages:
    DogRunImagesLeft.append(pygame.transform.flip(image,True,False))
TreeImages=[]
TreeImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/Object/Tree_1.png"),(116/2,44/2)))
TreeImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/Object/Tree_2.png"),(282/2,301/2)))

Level1TileMap="00000000000000000000000000000000000000000000000000n" \
              "00000000000000000000000000000000000000000000000000n" \
              "00000000000000000000000000000000000000000000000000n" \
              "b0000b00000000000000000000000000000000000000000000n" \
              "b0000b00000000000000000000000000000000000000000000n" \
              "b0T0Db00T000000p0000D00000TT0000000000000000000000n" \
              "11111111110000011001111111111100000000000000000000n" \
              "dddddddd0000T00000000010t01000010t0010000000000000n" \
              "dddddddd111111wwwwwwwww11wwwwwww111wwwwwwwwwwwwwwwn" \
              "ddddddddddddddWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWn"

Level2TileMap="00000000000000000000000000000000000000000000000000n" \
              "00000000000000000000000000000000000000000000000000n" \
              "00000000000000000000000000000000000000000000000000n" \
              "b0000b00000000000000000000000000000000000000000000n" \
              "b0000b00000000000000000000000000000000000000000000n" \
              "b0TLDb00T000000pL000D00L00TT0000000000000000000000n" \
              "11111111110000011001111111111100000000000000000000n" \
              "dddddddd0000T00000000010t01000010t0010000000000000n" \
              "dddddddd111111wwwwwwwww11wwwwwww111wwwwwwwwwwwwwwwn" \
              "ddddddddddddddWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWn"

FreeRunStart= "000000000000000000000000000000n" \
              "000000000000000000000000000000n" \
              "000000000000000000000000000000n" \
              "000000000000000000000000000000n" \
              "000000000000000000000000000000n" \
              "000000000000000000000000000000n" \
              "00p000000000000000000000000000n" \
              "1111111111111111111111111111111111111111n" \
              "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwn" \
              "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWn"
HudFont=pygame.font.Font("Level1Assets/BloodyTerror.ttf",20)
MenuFont=pygame.font.Font("Level1Assets/BloodyTerror.ttf",40)
MenuButtonFont=pygame.font.Font("Level1Assets/BloodyTerror.ttf",27)
MenuButtonTextColor=(164,63,79)
ButtonImages=[]
ButtonImages.append(pygame.transform.scale(pygame.image.load("MenuImages/bt1.png"),(490//2,220//2)))
ButtonImages.append(pygame.transform.scale(pygame.image.load("MenuImages/bt2.png"),(440//2,200//2)))
MenuBackground=pygame.transform.scale(pygame.image.load("Level1Assets/BG/BG.png"),(WindowWidth,WindowHeight))