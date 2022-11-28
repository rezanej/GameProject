import pygame
from os.path import exists
pygame.init()
WindowWidth=64*20 #temporary
WindowHeight=64*10 #temporary
#Display is her cause convert alpha needs it
Display=pygame.display.set_mode((WindowWidth,WindowHeight),flags=pygame.SCALED,vsync=1)
Fps=60
CurrentLevel=0
PlayerSpeed=5
PlayerAnimationSpeed=0.4
DogSpeed=3
PlayerJumpSpeed=32
Gravity=2
KunaiSpeed=30
StartKunai=40
KunaiLifetime=4
KunaiTimer=20
BackgroundImages=[]
Grassimages=[]
Grassimages.append(pygame.transform.scale(pygame.image.load("Level1Assets/Tiles/2.png"),(64,64)).convert_alpha())
Grassimages.append(pygame.transform.scale(pygame.image.load("Level2/Tiles/Tile (2).png"),(64,64)).convert_alpha())
BackgroundImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/BG/BG.png"),(64*20,640)).convert_alpha())
BackgroundImages.append(pygame.transform.scale(pygame.image.load("Level2/BG.png"),(64*20,640)).convert_alpha())
PlayerImage=pygame.transform.scale(pygame.image.load("PlayerImages/Idle__000.png"),(232/7,439/7)).convert_alpha()
DirtImages=[]
DirtImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/Tiles/5.png"),(64,64)).convert_alpha())
DirtImages.append(pygame.transform.scale(pygame.image.load("Level2/Tiles/Tile (5).png"),(64,64)))
WaterImages=[]
WaterImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/Tiles/17.png"),(64,64)).convert_alpha())
WaterImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/Tiles/18.png"),(64,64)).convert_alpha())
PlayerIdleImages=[]
PlayerIdleImagesLeft=[]
PlayerIdleImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Idle__000.png"),(232/7,439/7)).convert_alpha())
PlayerIdleImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Idle__001.png"),(232/7,439/7)).convert_alpha())
PlayerIdleImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Idle__002.png"),(232/7,439/7)).convert_alpha())
PlayerIdleImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Idle__003.png"),(232/7,439/7)).convert_alpha())
PlayerIdleImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Idle__004.png"),(232/7,439/7)).convert_alpha())
PlayerIdleImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Idle__005.png"),(232/7,439/7)).convert_alpha())
PlayerIdleImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Idle__006.png"),(232/7,439/7)).convert_alpha())
PlayerIdleImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Idle__007.png"),(232/7,439/7)).convert_alpha())
PlayerIdleImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Idle__008.png"),(232/7,439/7)).convert_alpha())
PlayerIdleImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Idle__009.png"),(232/7,439/7)).convert_alpha())
for image in PlayerIdleImages:
    PlayerIdleImagesLeft.append(pygame.transform.flip(image,True,False))
PlayerRunImages=[]
PlayerRunImagesLeft=[]
PlayerRunImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Run__000.png"),(363/7,439/7)).convert_alpha())
PlayerRunImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Run__001.png"),(363/7,439/7)).convert_alpha())
PlayerRunImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Run__002.png"),(363/7,439/7)).convert_alpha())
PlayerRunImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Run__003.png"),(363/7,439/7)).convert_alpha())
PlayerRunImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Run__004.png"),(363/7,439/7)).convert_alpha())
PlayerRunImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Run__005.png"),(363/7,439/7)).convert_alpha())
PlayerRunImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Run__006.png"),(363/7,439/7)).convert_alpha())
PlayerRunImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Run__007.png"),(363/7,439/7)).convert_alpha())
PlayerRunImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Run__008.png"),(363/7,439/7)).convert_alpha())
PlayerRunImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Run__009.png"),(363/7,439/7)).convert_alpha())
PlayerJumpImages=[]
PlayerJumpImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Jump__000.png"),(363/7,439/7)).convert_alpha())
PlayerJumpImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Jump__001.png"),(363/7,439/7)).convert_alpha())
PlayerJumpImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Jump__002.png"),(363/7,439/7)).convert_alpha())
PlayerJumpImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Jump__003.png"),(363/7,439/7)).convert_alpha())
PlayerJumpImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Jump__004.png"),(363/7,439/7)).convert_alpha())
PlayerJumpImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Jump__005.png"),(363/7,439/7)).convert_alpha())
PlayerJumpImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Jump__006.png"),(363/7,439/7)).convert_alpha())
PlayerJumpImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Jump__007.png"),(363/7,439/7)).convert_alpha())
PlayerJumpImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Jump__008.png"),(363/7,439/7)).convert_alpha())
PlayerJumpImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Jump__009.png"),(363/7,439/7)).convert_alpha())
PlayerJumpImagesLeft=[]
for images in PlayerJumpImages:
    PlayerJumpImagesLeft.append(pygame.transform.flip(images,True,False))
for images in PlayerRunImages:
    PlayerRunImagesLeft.append(pygame.transform.flip(images,True,False))

PlayerAttackImages=[]
PlayerAttackImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Attack__000.png"),(538/7,495/7)).convert_alpha())
PlayerAttackImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Attack__001.png"),(538/7,495/7)).convert_alpha())
PlayerAttackImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Attack__002.png"),(538/7,495/7)).convert_alpha())
PlayerAttackImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Attack__003.png"),(538/7,495/7)).convert_alpha())
PlayerAttackImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Attack__004.png"),(538/7,495/7)).convert_alpha())
PlayerAttackImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Attack__005.png"),(538/7,495/7)).convert_alpha())
PlayerAttackImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Attack__006.png"),(538/7,495/7)).convert_alpha())
PlayerAttackImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Attack__007.png"),(538/7,495/7)).convert_alpha())
PlayerAttackImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Attack__008.png"),(538/7,495/7)).convert_alpha())
PlayerAttackImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Attack__009.png"),(538/7,495/7)).convert_alpha())
PlayerAttackImagesLeft=[]
for image in PlayerAttackImages:
    PlayerAttackImagesLeft.append(pygame.transform.flip(image,True,False))

PlayerThrowImages=[]
PlayerThrowImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Throw__000.png"),(377/7,451/7)).convert_alpha())
PlayerThrowImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Throw__001.png"),(377/7,451/7)).convert_alpha())
PlayerThrowImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Throw__002.png"),(377/7,451/7)).convert_alpha())
PlayerThrowImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Throw__003.png"),(377/7,451/7)).convert_alpha())
PlayerThrowImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Throw__004.png"),(377/7,451/7)).convert_alpha())
PlayerThrowImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Throw__005.png"),(377/7,451/7)).convert_alpha())
PlayerThrowImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Throw__006.png"),(377/7,451/7)).convert_alpha())
PlayerThrowImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Throw__007.png"),(377/7,451/7)).convert_alpha())
PlayerThrowImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Throw__008.png"),(377/7,451/7)).convert_alpha())
PlayerThrowImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Throw__009.png"),(377/7,451/7)).convert_alpha())
PlayerThrowImagesLeft=[]
for image in PlayerThrowImages:
    PlayerThrowImagesLeft.append(pygame.transform.flip(image,True,False))
PlayerDeadImages=[]
PlayerDeadImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Dead__000.png"),(482/7,498/7)).convert_alpha())
PlayerDeadImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Dead__001.png"),(482/7,498/7)).convert_alpha())
PlayerDeadImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Dead__002.png"),(482/7,498/7)).convert_alpha())
PlayerDeadImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Dead__003.png"),(482/7,498/7)).convert_alpha())
PlayerDeadImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Dead__004.png"),(482/7,498/7)).convert_alpha())
PlayerDeadImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Dead__005.png"),(482/7,498/7)).convert_alpha())
PlayerDeadImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Dead__006.png"),(482/7,498/7)).convert_alpha())
PlayerDeadImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Dead__007.png"),(482/7,498/7)).convert_alpha())
PlayerDeadImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Dead__008.png"),(482/7,498/7)).convert_alpha())
PlayerDeadImages.append(pygame.transform.scale(pygame.image.load("PlayerImages/Dead__009.png"),(482/7,498/7)).convert_alpha())
PlayerDeadImagesLeft=[]
for image in PlayerDeadImages:
    PlayerDeadImagesLeft.append(pygame.transform.flip(image,True,False))

KunaiImgae=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("PlayerImages/Kunai.png"),(32/4,160/4)),90).convert_alpha()
KunaiImgae=pygame.transform.flip(KunaiImgae,True,False)
KunaiImgaeLeft=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("PlayerImages/Kunai.png"),(32/4,160/4)),90).convert_alpha()

DogIdleImages=[]

DogIdleImages.append(pygame.transform.scale(pygame.image.load("dog/Idle (1).png"),(547/7,481/7)).convert_alpha())
DogIdleImages.append(pygame.transform.scale(pygame.image.load("dog/Idle (2).png"),(547/7,481/7)).convert_alpha())
DogIdleImages.append(pygame.transform.scale(pygame.image.load("dog/Idle (3).png"),(547/7,481/7)).convert_alpha())
DogIdleImages.append(pygame.transform.scale(pygame.image.load("dog/Idle (4).png"),(547/7,481/7)).convert_alpha())
DogIdleImages.append(pygame.transform.scale(pygame.image.load("dog/Idle (5).png"),(547/7,481/7)).convert_alpha())
DogIdleImages.append(pygame.transform.scale(pygame.image.load("dog/Idle (6).png"),(547/7,481/7)).convert_alpha())
DogIdleImages.append(pygame.transform.scale(pygame.image.load("dog/Idle (7).png"),(547/7,481/7)).convert_alpha())
DogIdleImages.append(pygame.transform.scale(pygame.image.load("dog/Idle (8).png"),(547/7,481/7)).convert_alpha())
DogIdleImages.append(pygame.transform.scale(pygame.image.load("dog/Idle (9).png"),(547/7,481/7)).convert_alpha())
DogIdleImages.append(pygame.transform.scale(pygame.image.load("dog/Idle (10).png"),(547/7,481/7)).convert_alpha())
DogIdleImagesLeft=[]
for image in DogIdleImages:
    DogIdleImagesLeft.append(pygame.transform.flip(image,True,False))

DogRunImages=[]
DogRunImages.append(pygame.transform.scale(pygame.image.load("dog/Run (1).png"),(547/7,481/7)).convert_alpha())
DogRunImages.append(pygame.transform.scale(pygame.image.load("dog/Run (2).png"),(547/7,481/7)).convert_alpha())
DogRunImages.append(pygame.transform.scale(pygame.image.load("dog/Run (3).png"),(547/7,481/7)).convert_alpha())
DogRunImages.append(pygame.transform.scale(pygame.image.load("dog/Run (4).png"),(547/7,481/7)).convert_alpha())
DogRunImages.append(pygame.transform.scale(pygame.image.load("dog/Run (5).png"),(547/7,481/7)).convert_alpha())
DogRunImages.append(pygame.transform.scale(pygame.image.load("dog/Run (6).png"),(547/7,481/7)).convert_alpha())
DogRunImages.append(pygame.transform.scale(pygame.image.load("dog/Run (7).png"),(547/7,481/7)).convert_alpha())
DogRunImages.append(pygame.transform.scale(pygame.image.load("dog/Run (8).png"),(547/7,481/7)).convert_alpha())
DogRunImagesLeft=[]
for image in DogRunImages:
    DogRunImagesLeft.append(pygame.transform.flip(image,True,False))
DogDeadImages=[]
DogDeadImages.append(pygame.transform.scale(pygame.image.load("dog/Dead (1).png"),(580/7,510/7)).convert_alpha())
DogDeadImages.append(pygame.transform.scale(pygame.image.load("dog/Dead (2).png"),(580/7,510/7)).convert_alpha())
DogDeadImages.append(pygame.transform.scale(pygame.image.load("dog/Dead (3).png"),(580/7,510/7)).convert_alpha())
DogDeadImages.append(pygame.transform.scale(pygame.image.load("dog/Dead (4).png"),(580/7,510/7)).convert_alpha())
DogDeadImages.append(pygame.transform.scale(pygame.image.load("dog/Dead (5).png"),(580/7,510/7)).convert_alpha())
DogDeadImages.append(pygame.transform.scale(pygame.image.load("dog/Dead (6).png"),(580/7,510/7)).convert_alpha())
DogDeadImages.append(pygame.transform.scale(pygame.image.load("dog/Dead (7).png"),(580/7,510/7)).convert_alpha())
DogDeadImages.append(pygame.transform.scale(pygame.image.load("dog/Dead (8).png"),(580/7,510/7)).convert_alpha())
DogDeadImages.append(pygame.transform.scale(pygame.image.load("dog/Dead (9).png"),(580/7,510/7)).convert_alpha())
DogDeadImages.append(pygame.transform.scale(pygame.image.load("dog/Dead (10).png"),(580/7,510/7)).convert_alpha())
DogDeadImagesLeft=[]
for image in DogDeadImages:
    DogDeadImagesLeft.append(pygame.transform.flip(image,True,False))
CatIdleImages=[]

CatIdleImages.append(pygame.transform.scale(pygame.image.load("cat/Idle (1).png"),(547/7,481/7)).convert_alpha())
CatIdleImages.append(pygame.transform.scale(pygame.image.load("cat/Idle (2).png"),(547/7,481/7)).convert_alpha())
CatIdleImages.append(pygame.transform.scale(pygame.image.load("cat/Idle (3).png"),(547/7,481/7)).convert_alpha())
CatIdleImages.append(pygame.transform.scale(pygame.image.load("cat/Idle (4).png"),(547/7,481/7)).convert_alpha())
CatIdleImages.append(pygame.transform.scale(pygame.image.load("cat/Idle (5).png"),(547/7,481/7)).convert_alpha())
CatIdleImages.append(pygame.transform.scale(pygame.image.load("cat/Idle (6).png"),(547/7,481/7)).convert_alpha())
CatIdleImages.append(pygame.transform.scale(pygame.image.load("cat/Idle (7).png"),(547/7,481/7)).convert_alpha())
CatIdleImages.append(pygame.transform.scale(pygame.image.load("cat/Idle (8).png"),(547/7,481/7)).convert_alpha())
CatIdleImages.append(pygame.transform.scale(pygame.image.load("cat/Idle (9).png"),(547/7,481/7)).convert_alpha())
CatIdleImages.append(pygame.transform.scale(pygame.image.load("cat/Idle (10).png"),(547/7,481/7)).convert_alpha())
CatIdleImagesLeft=[]
for image in CatIdleImages:
    CatIdleImagesLeft.append(pygame.transform.flip(image,True,False))

CatRunImages=[]
CatRunImages.append(pygame.transform.scale(pygame.image.load("cat/Run (1).png"),(547/7,481/7)).convert_alpha())
CatRunImages.append(pygame.transform.scale(pygame.image.load("cat/Run (2).png"),(547/7,481/7)).convert_alpha())
CatRunImages.append(pygame.transform.scale(pygame.image.load("cat/Run (3).png"),(547/7,481/7)).convert_alpha())
CatRunImages.append(pygame.transform.scale(pygame.image.load("cat/Run (4).png"),(547/7,481/7)).convert_alpha())
CatRunImages.append(pygame.transform.scale(pygame.image.load("cat/Run (5).png"),(547/7,481/7)).convert_alpha())
CatRunImages.append(pygame.transform.scale(pygame.image.load("cat/Run (6).png"),(547/7,481/7)).convert_alpha())
CatRunImages.append(pygame.transform.scale(pygame.image.load("cat/Run (7).png"),(547/7,481/7)).convert_alpha())
CatRunImages.append(pygame.transform.scale(pygame.image.load("cat/Run (8).png"),(547/7,481/7)).convert_alpha())
CatRunImagesLeft=[]
for image in CatRunImages:
    CatRunImagesLeft.append(pygame.transform.flip(image,True,False))
CatDeadImages=[]
CatDeadImages.append(pygame.transform.scale(pygame.image.load("cat/Dead (1).png"),(580/7,510/7)).convert_alpha())
CatDeadImages.append(pygame.transform.scale(pygame.image.load("cat/Dead (2).png"),(580/7,510/7)).convert_alpha())
CatDeadImages.append(pygame.transform.scale(pygame.image.load("cat/Dead (3).png"),(580/7,510/7)).convert_alpha())
CatDeadImages.append(pygame.transform.scale(pygame.image.load("cat/Dead (4).png"),(580/7,510/7)).convert_alpha())
CatDeadImages.append(pygame.transform.scale(pygame.image.load("cat/Dead (5).png"),(580/7,510/7)).convert_alpha())
CatDeadImages.append(pygame.transform.scale(pygame.image.load("cat/Dead (6).png"),(580/7,510/7)).convert_alpha())
CatDeadImages.append(pygame.transform.scale(pygame.image.load("cat/Dead (7).png"),(580/7,510/7)).convert_alpha())
CatDeadImages.append(pygame.transform.scale(pygame.image.load("cat/Dead (8).png"),(580/7,510/7)).convert_alpha())
CatDeadImages.append(pygame.transform.scale(pygame.image.load("cat/Dead (9).png"),(580/7,510/7)).convert_alpha())
CatDeadImages.append(pygame.transform.scale(pygame.image.load("cat/Dead (10).png"),(580/7,510/7)).convert_alpha())
CatDeadImagesLeft=[]
for image in CatDeadImages:
    CatDeadImagesLeft.append(pygame.transform.flip(image,True,False))

NinjaGirlIdleImages=[]
NinjaGirlIdleImagesLeft=[]
NinjaGirlIdleImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Idle__000.png"),(290/7,500/7)).convert_alpha())
NinjaGirlIdleImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Idle__001.png"),(290/7,500/7)).convert_alpha())
NinjaGirlIdleImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Idle__002.png"),(290/7,500/7)).convert_alpha())
NinjaGirlIdleImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Idle__003.png"),(290/7,500/7)).convert_alpha())
NinjaGirlIdleImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Idle__004.png"),(290/7,500/7)).convert_alpha())
NinjaGirlIdleImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Idle__005.png"),(290/7,500/7)).convert_alpha())
NinjaGirlIdleImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Idle__006.png"),(290/7,500/7)).convert_alpha())
NinjaGirlIdleImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Idle__007.png"),(290/7,500/7)).convert_alpha())
NinjaGirlIdleImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Idle__008.png"),(290/7,500/7)).convert_alpha())
NinjaGirlIdleImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Idle__009.png"),(290/7,500/7)).convert_alpha())
for image in NinjaGirlIdleImages:
    NinjaGirlIdleImagesLeft.append(pygame.transform.flip(image,True,False))
NinjaGirlRunImages=[]
NinjaGirlRunImagesLeft=[]
NinjaGirlRunImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Run__000.png"),(376/7,520/7)).convert_alpha())
NinjaGirlRunImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Run__001.png"),(376/7,520/7)).convert_alpha())
NinjaGirlRunImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Run__002.png"),(376/7,520/7)).convert_alpha())
NinjaGirlRunImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Run__003.png"),(376/7,520/7)).convert_alpha())
NinjaGirlRunImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Run__004.png"),(376/7,520/7)).convert_alpha())
NinjaGirlRunImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Run__005.png"),(376/7,520/7)).convert_alpha())
NinjaGirlRunImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Run__006.png"),(376/7,520/7)).convert_alpha())
NinjaGirlRunImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Run__007.png"),(376/7,520/7)).convert_alpha())
NinjaGirlRunImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Run__008.png"),(376/7,520/7)).convert_alpha())
NinjaGirlRunImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Run__009.png"),(376/7,520/7)).convert_alpha())
for images in NinjaGirlRunImages:
    NinjaGirlRunImagesLeft.append(pygame.transform.flip(images,True,False))

NinjaGirlThrowImages=[]
NinjaGirlThrowImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Throw__000.png"),(377/7,451/7)).convert_alpha())
NinjaGirlThrowImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Throw__001.png"),(377/7,451/7)).convert_alpha())
NinjaGirlThrowImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Throw__002.png"),(377/7,451/7)).convert_alpha())
NinjaGirlThrowImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Throw__003.png"),(377/7,451/7)).convert_alpha())
NinjaGirlThrowImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Throw__004.png"),(377/7,451/7)).convert_alpha())
NinjaGirlThrowImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Throw__005.png"),(377/7,451/7)).convert_alpha())
NinjaGirlThrowImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Throw__006.png"),(377/7,451/7)).convert_alpha())
NinjaGirlThrowImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Throw__007.png"),(377/7,451/7)).convert_alpha())
NinjaGirlThrowImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Throw__008.png"),(377/7,451/7)).convert_alpha())
NinjaGirlThrowImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Throw__009.png"),(377/7,451/7)).convert_alpha())
NinjaGirlThrowImagesLeft=[]
for image in NinjaGirlThrowImages:
    NinjaGirlThrowImagesLeft.append(pygame.transform.flip(image,True,False))
NinjaGirlDeadImages=[]
NinjaGirlDeadImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Dead__000.png"),(578/7,599/7)).convert_alpha())
NinjaGirlDeadImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Dead__001.png"),(578/7,599/7)).convert_alpha())
NinjaGirlDeadImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Dead__002.png"),(578/7,599/7)).convert_alpha())
NinjaGirlDeadImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Dead__003.png"),(578/7,599/7)).convert_alpha())
NinjaGirlDeadImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Dead__004.png"),(578/7,599/7)).convert_alpha())
NinjaGirlDeadImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Dead__005.png"),(578/7,599/7)).convert_alpha())
NinjaGirlDeadImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Dead__006.png"),(578/7,599/7)).convert_alpha())
NinjaGirlDeadImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Dead__007.png"),(578/7,599/7)).convert_alpha())
NinjaGirlDeadImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Dead__008.png"),(578/7,599/7)).convert_alpha())
NinjaGirlDeadImages.append(pygame.transform.scale(pygame.image.load("NinjaGirlImages/Dead__009.png"),(578/7,599/7)).convert_alpha())
NinjaGirlDeadImagesLeft=[]
for image in NinjaGirlDeadImages:
    NinjaGirlDeadImagesLeft.append(pygame.transform.flip(image,True,False))

TreeImages=[]
TreeImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/Object/Tree_1.png"),(116/2,44/2)).convert_alpha())
TreeImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/Object/Tree_2.png"),(282/2,301/2)).convert_alpha())
TreeImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/Object/Tree1.png"),(111,117)).convert_alpha())
TreeImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/Object/Tree2.png"),(90,151)).convert_alpha())
TreeImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/Object/Tree3.png"),(63,96)).convert_alpha())
TreeImages.append(pygame.transform.scale(pygame.image.load("Level2/Objects/Tree.png"),(286/2,239/2)).convert_alpha())
TreeImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/Object/Tree3.png"),(63,96)).convert_alpha())
ObjectImages=[]
ObjectImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/Object/Bush (1).png"),(133,65)).convert_alpha())
ObjectImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/Object/Bush (2).png"),(133,65)).convert_alpha())
# ObjectImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/Object/Crate.png"),(77,77)).convert_alpha())
ObjectImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/Object/Mushroom_1.png"),(49,41)).convert_alpha())
ObjectImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/Object/Mushroom_2.png"),(49,41)).convert_alpha())
ObjectImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/Object/Stone.png"),(90,54)).convert_alpha())
ObjectImages.append(pygame.transform.scale(pygame.image.load("Level2/Objects/DeadBush.png"),(132,74)).convert_alpha())
ObjectImages.append(pygame.transform.scale(pygame.image.load("Level2/Objects/TombStone (1).png"),(54,55)).convert_alpha())
ObjectImages.append(pygame.transform.scale(pygame.image.load("Level2/Objects/TombStone (2).png"),(53,76)).convert_alpha())


Level1TileMap="000000000000000000000000000000000000000000000000000000000ccckCc0000ddddddddddddddd00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000n" \
              "b000000000000000000000000000000000000000000000000000001111111110000ddddddddddddddd0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000BB000khC000000000h000000BB00000000000000000000000n" \
              "b000000000000000B000000000000B000000000000000000000001ddddddddd1000ddddddddddddddd00BB00000000000kh00000000000000BB000000000000000000000000000000000kC00000000000000000000000000000000000000BB0001111000000111100000BB00000000000000000000000n" \
              "b000000000000000B000000000000B00000000000000000000001dddddddddd0000ddddddddddddddd00BB0000000000C1110000000000000BB00000000000000000000000000000BB00111000h00000000000000BB00000000000000000BB000000000000000000cc00BB0000000000000000b000000n" \
              "b000000000000000B000000000000B0000000000000000000001ddddddddddd0000ddddddd00dddddd00BB000000000010000000000000000BB00000000000000000000Ch00C0000BB00000001110000000000000BB00000000000000000BB00CCh00N0TCC0tcc000000BB0000000000000000b000000n" \
              "b00pPT0Tkr000000BC000jTN0ccT0B000000000TePrT00k0001dddddddddddd0001dddddd000ckc00d00BB000000000000000000000000000BB00000000000000000CC0000000000BB00000000000000000000000BB00000000000000000111111111111111111111111111000000000000000b000000n" \
              "11111111110000Ck11111111111111000t0000111111111111ddddddddddddd0000dddddd00dddddd000BBr0t0T0acT0T0ca00Tt0Tc00T000BB0000000000CC00011111001110000BBcc0T0D0a00T00CCe00tT0C0BB00000000000000011ddddddddddddddddddddddddddd11100Pccjccko00b000000n" \
              "dddddddddd0c0c1100000000000000111111C000c00c0cc0ddddddddddddddd00000000CCCCCCCC000P11111111111111111111111111111111rPchccc00111100ddddd00000C1111111111111111111111111111100P0jcchh0k01111dddddddddddddddddddddddddddddddd1111111111111111110n" \
              "dddddddddd1111wwwwwwwwwwwwwwwwwwwwww111111111111ddddddddddddddd0001111111111111111111wwwwwwwwwwwwwwwwwwwwwwwwwwww11111110011100000dddd000dddddd000000000000000000000000000111111111111dddddddddddddddddddddddddddddddddddddddddddddddddddddddn" \
              "ddddddddddddddWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW1WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW00n"

Level2TileMap="000000000000000000000000000003P0BBBBBBBBBBBBBBBBBBBBdddd00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000BB0000hk0000000000000000000BB0ddddddddddd00000000000000000000000000000000000000000000000n" \
              "b0000000000000dddddddddd00000110BB0000000000000000BBdddd00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000BB0000110000000000000000000BB0ddddddddddd0000000BB00000000000000000000000000000000BB0000n" \
              "b0000000000000dddddddddd00200000BB005020Z05045000BBdddd000000000000000000000000000000000000000BB00000h500000000kC0000BB0000000000000000000000000000000BB0000000000000000000000000BB0ddddddddddd0000000BB00000000000000000000000000000000BB0000n" \
              "b0000000000000dddddddddd0011000011111111111111111101dddd000000000000000000000000000000000000000BB000001100000000110000BB00000000000000004050h0000040500BB05020030040305N0330402000BB0dddddddddddd000000BB00000000000000000000000000000000BB00b0n" \
              "b05L00p5050L00dddddddddd00000000dddddddd00000030000ddddd00000000BB0000000000000000000BB00000000BB000000000000000000000BB003030c22h5PCc01111110011111110111111111111111111111111111101dddddddddddd000000BB00000000000000000000000000000000BB00b0n" \
              "11111111110000dddddddddd11111000dddddddd0ddddddddddddddd00000000BB0000000000000000000BB00000000BB005400002300Z05000405BB01111111111111ddddddd00ddddddd0dddddddddddddddddddddddddddd0ddddddddddddddd0000BB00000000000000000000000000000000BB00b0n" \
              "dk00000000000ddddddddddd00000000dd000000000kk000dddddddd00000000BB0000000000000000000BB0000000011111111111111111111111111dddddddddddddddddddd00ddddddd0ddddddd0000000000000000000000ddddddddddddddd0000BB00000000000000000000000000000000BB00b0n" \
              "dd00000011111ddddddddddd00000001ddCC00000dddddddddddddddd0000000BB0050cc400z0000CC325BBPk111111dddddddddddddddddddddddddddddddddddddddddddddd00ddddddd0ddddddd0dddddddddddddddddddddd000000hhhhhhhh0PcCBBC2cccc503CCC40S00402203000504000BB00b0n" \
              "dd00000000000000ccckhh00000P0000dddd0000000000000CCCcccc003050001111111111111111111111111ddddddddddddddddddddddddddddddddddddddddddddddddddd000ddddddd0ddddd00000cccccccccc00000000000111111111111111111111111111111111111111111111111111111111111111111n" \
              "ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd0000000000000000000000dddddd00dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddn"

FreeRunStart= "000000000000000000000000000000n" \
              "000000000000000000000000000000n" \
              "000000000000000000000000000000n" \
              "000000000000000000000000000000n" \
              "000000000000000000000000000000n" \
              "000000000000000000000000000000n" \
              "00p000000000000000000000000000n" \
              "1111111111111111111111111111111111111111n" \
              "ddddddddddddddddddddddddddddddddddddddddn" \
              "ddddddddddddddddddddddddddddddddddddddddn"
LevelMaps=[Level1TileMap,Level2TileMap]
HudFont=pygame.font.Font("Level1Assets/BloodyTerror.ttf",20)
MenuFont=pygame.font.Font("Level1Assets/BloodyTerror.ttf",40)
MenuButtonFont=pygame.font.Font("Level1Assets/BloodyTerror.ttf",27)
MenuButtonTextColor=(164,63,79)
ButtonImages=[]
ButtonImages.append(pygame.transform.scale(pygame.image.load("MenuImages/bt1.png"),(490//2,220//2)).convert_alpha())
ButtonImages.append(pygame.transform.scale(pygame.image.load("MenuImages/bt2.png"),(440//2,200//2)).convert_alpha())
MenuBackground=pygame.transform.scale(pygame.image.load("Level1Assets/BG/BG.png"),(WindowWidth,WindowHeight)).convert_alpha()
CoinImages=[]
CoinImages.append(pygame.transform.scale(pygame.image.load("CoinImages/SILVER/SMALL/SMALL_0000_Capa-1.png"),(26,26)).convert_alpha())
CoinImages.append(pygame.transform.scale(pygame.image.load("CoinImages/SILVER/SMALL/SMALL_0001_Capa-2.png"),(26,26)).convert_alpha())
CoinImages.append(pygame.transform.scale(pygame.image.load("CoinImages/SILVER/SMALL/SMALL_0002_Capa-3.png"),(26,26)).convert_alpha())
CoinImages.append(pygame.transform.scale(pygame.image.load("CoinImages/SILVER/SMALL/SMALL_0003_Capa-4.png"),(26,26)).convert_alpha())
CoinImages.append(pygame.transform.scale(pygame.image.load("CoinImages/SILVER/SMALL/SMALL_0004_Capa-5.png"),(26,26)).convert_alpha())
CoinImages.append(pygame.transform.scale(pygame.image.load("CoinImages/SILVER/SMALL/SMALL_0005_Capa-6.png"),(26,26)).convert_alpha())
CoinImages.append(pygame.transform.scale(pygame.image.load("CoinImages/SILVER/SMALL/SMALL_0006_Capa-7.png"),(26,26)).convert_alpha())
CoinImages.append(pygame.transform.scale(pygame.image.load("CoinImages/SILVER/SMALL/SMALL_0007_Capa-8.png"),(26,26)).convert_alpha())
GoldCoinImages=[]
GoldCoinImages.append(pygame.transform.scale(pygame.image.load("CoinImages/GOLD/SMALL/SMALL_0000_Capa-1.png"),(26,26)).convert_alpha())
GoldCoinImages.append(pygame.transform.scale(pygame.image.load("CoinImages/GOLD/SMALL/SMALL_0001_Capa-2.png"),(26,26)).convert_alpha())
GoldCoinImages.append(pygame.transform.scale(pygame.image.load("CoinImages/GOLD/SMALL/SMALL_0002_Capa-3.png"),(26,26)).convert_alpha())
GoldCoinImages.append(pygame.transform.scale(pygame.image.load("CoinImages/GOLD/SMALL/SMALL_0003_Capa-4.png"),(26,26)).convert_alpha())
GoldCoinImages.append(pygame.transform.scale(pygame.image.load("CoinImages/GOLD/SMALL/SMALL_0004_Capa-5.png"),(26,26)).convert_alpha())
GoldCoinImages.append(pygame.transform.scale(pygame.image.load("CoinImages/GOLD/SMALL/SMALL_0005_Capa-6.png"),(26,26)).convert_alpha())
GoldCoinImages.append(pygame.transform.scale(pygame.image.load("CoinImages/GOLD/SMALL/SMALL_0006_Capa-7.png"),(26,26)).convert_alpha())
GoldCoinImages.append(pygame.transform.scale(pygame.image.load("CoinImages/GOLD/SMALL/SMALL_0007_Capa-8.png"),(26,26)).convert_alpha())
HeartImages=[]
HeartImages.append(pygame.transform.scale(pygame.image.load("HeartImages/tile000.png"),(26,26)).convert_alpha())
HeartImages.append(pygame.transform.scale(pygame.image.load("HeartImages/tile001.png"),(26,26)).convert_alpha())
HeartImages.append(pygame.transform.scale(pygame.image.load("HeartImages/tile002.png"),(26,26)).convert_alpha())
HeartImages.append(pygame.transform.scale(pygame.image.load("HeartImages/tile003.png"),(26,26)).convert_alpha())
HeartImages.append(pygame.transform.scale(pygame.image.load("HeartImages/tile004.png"),(26,26)).convert_alpha())
HeartImages.append(pygame.transform.scale(pygame.image.load("HeartImages/tile005.png"),(26,26)).convert_alpha())
PortalImages=[]
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_201.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_202.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_203.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_204.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_205.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_206.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_207.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_208.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_209.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_210.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_211.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_212.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_213.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_214.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_215.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_216.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_217.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_218.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_219.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_220.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_221.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_222.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_223.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_224.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_225.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_226.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_227.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_228.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_229.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_230.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_231.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_232.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_233.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_234.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_235.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_236.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_237.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_238.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_239.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_240.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_241.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_242.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_243.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_244.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_245.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_246.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_247.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_248.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_249.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_250.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_251.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_252.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_253.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_254.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_255.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_256.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_257.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_258.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_259.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_260.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_261.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_262.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_263.png"),(400,300)).convert_alpha())
PortalImages.append(pygame.transform.scale(pygame.image.load("portal/portal_264.png"),(400,300)).convert_alpha())


zombieMaleIdleImages=[]
zombieMaleIdleImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Idle (1).png"),(430/7,517/7)).convert_alpha())
zombieMaleIdleImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Idle (2).png"),(430/7,517/7)).convert_alpha())
zombieMaleIdleImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Idle (3).png"),(430/7,517/7)).convert_alpha())
zombieMaleIdleImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Idle (4).png"),(430/7,517/7)).convert_alpha())
zombieMaleIdleImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Idle (5).png"),(430/7,517/7)).convert_alpha())
zombieMaleIdleImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Idle (6).png"),(430/7,517/7)).convert_alpha())
zombieMaleIdleImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Idle (7).png"),(430/7,517/7)).convert_alpha())
zombieMaleIdleImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Idle (8).png"),(430/7,517/7)).convert_alpha())
zombieMaleIdleImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Idle (9).png"),(430/7,517/7)).convert_alpha())
zombieMaleIdleImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Idle (10).png"),(430/7,517/7)).convert_alpha())
zombieMaleIdleImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Idle (11).png"),(430/7,517/7)).convert_alpha())
zombieMaleIdleImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Idle (12).png"),(430/7,517/7)).convert_alpha())
zombieMaleIdleImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Idle (13).png"),(430/7,517/7)).convert_alpha())
zombieMaleIdleImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Idle (14).png"),(430/7,517/7)).convert_alpha())
zombieMaleIdleImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Idle (15).png"),(430/7,517/7)).convert_alpha())
zombieMaleIdleImagesLeft=[]
for image in zombieMaleIdleImages:
    zombieMaleIdleImagesLeft.append(pygame.transform.flip(image,True,False))

zombieMaleWalkImages=[]
zombieMaleWalkImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Walk (1).png"),(430/7,517/7)).convert_alpha())
zombieMaleWalkImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Walk (2).png"),(430/7,517/7)).convert_alpha())
zombieMaleWalkImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Walk (3).png"),(430/7,517/7)).convert_alpha())
zombieMaleWalkImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Walk (4).png"),(430/7,517/7)).convert_alpha())
zombieMaleWalkImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Walk (5).png"),(430/7,517/7)).convert_alpha())
zombieMaleWalkImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Walk (6).png"),(430/7,517/7)).convert_alpha())
zombieMaleWalkImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Walk (7).png"),(430/7,517/7)).convert_alpha())
zombieMaleWalkImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Walk (8).png"),(430/7,517/7)).convert_alpha())
zombieMaleWalkImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Walk (9).png"),(430/7,517/7)).convert_alpha())
zombieMaleWalkImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Walk (10).png"),(430/7,517/7)).convert_alpha())
zombieMaleWalkImagesLeft=[]
for image in zombieMaleWalkImages:
    zombieMaleWalkImagesLeft.append(pygame.transform.flip(image,True,False))
zombieMaleDeadImages=[]
zombieMaleDeadImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Dead (1).png"),(629/7,526/7)).convert_alpha())
zombieMaleDeadImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Dead (2).png"),(629/7,526/7)).convert_alpha())
zombieMaleDeadImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Dead (3).png"),(629/7,526/7)).convert_alpha())
zombieMaleDeadImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Dead (4).png"),(629/7,526/7)).convert_alpha())
zombieMaleDeadImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Dead (5).png"),(629/7,526/7)).convert_alpha())
zombieMaleDeadImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Dead (6).png"),(629/7,526/7)).convert_alpha())
zombieMaleDeadImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Dead (7).png"),(629/7,526/7)).convert_alpha())
zombieMaleDeadImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Dead (8).png"),(629/7,526/7)).convert_alpha())
zombieMaleDeadImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Dead (9).png"),(629/7,526/7)).convert_alpha())
zombieMaleDeadImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Dead (10).png"),(629/7,526/7)).convert_alpha())
zombieMaleDeadImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Dead (11).png"),(629/7,526/7)).convert_alpha())
zombieMaleDeadImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/male/Dead (12).png"),(629/7,526/7)).convert_alpha())
zombieMaleDeadImagesLeft=[]
for image in zombieMaleDeadImages:
    zombieMaleDeadImagesLeft.append(pygame.transform.flip(image,True,False))


zombieFemaleIdleImages=[]
zombieFemaleIdleImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Idle (1).png"),(430/7,517/7)).convert_alpha())
zombieFemaleIdleImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Idle (2).png"),(430/7,517/7)).convert_alpha())
zombieFemaleIdleImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Idle (3).png"),(430/7,517/7)).convert_alpha())
zombieFemaleIdleImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Idle (4).png"),(430/7,517/7)).convert_alpha())
zombieFemaleIdleImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Idle (5).png"),(430/7,517/7)).convert_alpha())
zombieFemaleIdleImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Idle (6).png"),(430/7,517/7)).convert_alpha())
zombieFemaleIdleImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Idle (7).png"),(430/7,517/7)).convert_alpha())
zombieFemaleIdleImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Idle (8).png"),(430/7,517/7)).convert_alpha())
zombieFemaleIdleImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Idle (9).png"),(430/7,517/7)).convert_alpha())
zombieFemaleIdleImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Idle (10).png"),(430/7,517/7)).convert_alpha())
zombieFemaleIdleImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Idle (11).png"),(430/7,517/7)).convert_alpha())
zombieFemaleIdleImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Idle (12).png"),(430/7,517/7)).convert_alpha())
zombieFemaleIdleImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Idle (13).png"),(430/7,517/7)).convert_alpha())
zombieFemaleIdleImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Idle (14).png"),(430/7,517/7)).convert_alpha())
zombieFemaleIdleImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Idle (15).png"),(430/7,517/7)).convert_alpha())
zombieFemaleIdleImagesLeft=[]
for image in zombieFemaleIdleImages:
    zombieFemaleIdleImagesLeft.append(pygame.transform.flip(image,True,False))

zombieFemaleWalkImages=[]
zombieFemaleWalkImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Walk (1).png"),(430/7,517/7)).convert_alpha())
zombieFemaleWalkImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Walk (2).png"),(430/7,517/7)).convert_alpha())
zombieFemaleWalkImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Walk (3).png"),(430/7,517/7)).convert_alpha())
zombieFemaleWalkImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Walk (4).png"),(430/7,517/7)).convert_alpha())
zombieFemaleWalkImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Walk (5).png"),(430/7,517/7)).convert_alpha())
zombieFemaleWalkImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Walk (6).png"),(430/7,517/7)).convert_alpha())
zombieFemaleWalkImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Walk (7).png"),(430/7,517/7)).convert_alpha())
zombieFemaleWalkImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Walk (8).png"),(430/7,517/7)).convert_alpha())
zombieFemaleWalkImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Walk (9).png"),(430/7,517/7)).convert_alpha())
zombieFemaleWalkImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Walk (10).png"),(430/7,517/7)).convert_alpha())
zombieFemaleWalkImagesLeft=[]
for image in zombieFemaleWalkImages:
    zombieFemaleWalkImagesLeft.append(pygame.transform.flip(image,True,False))
zombieFemaleDeadImages=[]
zombieFemaleDeadImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Dead (1).png"),(629/7,526/7)).convert_alpha())
zombieFemaleDeadImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Dead (2).png"),(629/7,526/7)).convert_alpha())
zombieFemaleDeadImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Dead (3).png"),(629/7,526/7)).convert_alpha())
zombieFemaleDeadImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Dead (4).png"),(629/7,526/7)).convert_alpha())
zombieFemaleDeadImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Dead (5).png"),(629/7,526/7)).convert_alpha())
zombieFemaleDeadImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Dead (6).png"),(629/7,526/7)).convert_alpha())
zombieFemaleDeadImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Dead (7).png"),(629/7,526/7)).convert_alpha())
zombieFemaleDeadImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Dead (8).png"),(629/7,526/7)).convert_alpha())
zombieFemaleDeadImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Dead (9).png"),(629/7,526/7)).convert_alpha())
zombieFemaleDeadImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Dead (10).png"),(629/7,526/7)).convert_alpha())
zombieFemaleDeadImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Dead (11).png"),(629/7,526/7)).convert_alpha())
zombieFemaleDeadImages.append(pygame.transform.scale(pygame.image.load("Zombie/png/Female/Dead (12).png"),(629/7,526/7)).convert_alpha())
zombieFemaleDeadImagesLeft=[]
for image in zombieFemaleDeadImages:
    zombieFemaleDeadImagesLeft.append(pygame.transform.flip(image,True,False))

BossIdleImages0=[]
BossIdleImages0.append(pygame.transform.scale(pygame.image.load("Boss/0/tile000.png"),(85*2,94*2)).convert_alpha())
BossIdleImages0.append(pygame.transform.scale(pygame.image.load("Boss/0/tile001.png"),(85*2,94*2)).convert_alpha())
BossIdleImages0.append(pygame.transform.scale(pygame.image.load("Boss/0/tile002.png"),(85*2,94*2)).convert_alpha())
BossIdleImages0.append(pygame.transform.scale(pygame.image.load("Boss/0/tile003.png"),(85*2,94*2)).convert_alpha())
BossIdleImages0.append(pygame.transform.scale(pygame.image.load("Boss/0/tile004.png"),(85*2,94*2)).convert_alpha())
BossIdleImages0.append(pygame.transform.scale(pygame.image.load("Boss/0/tile005.png"),(85*2,94*2)).convert_alpha())
BossIdleImages0.append(pygame.transform.scale(pygame.image.load("Boss/0/tile006.png"),(85*2,94*2)).convert_alpha())
BossIdleImages0.append(pygame.transform.scale(pygame.image.load("Boss/0/tile007.png"),(85*2,94*2)).convert_alpha())
BossIdleImages0Left=[]
for image in BossIdleImages0:
    BossIdleImages0Left.append(pygame.transform.flip(image,True,False))
BossIdleImages1=[]
BossIdleImages1.append(pygame.transform.scale(pygame.image.load("Boss/1/tile000.png"),(122*2,110*2)).convert_alpha())
BossIdleImages1.append(pygame.transform.scale(pygame.image.load("Boss/1/tile001.png"),(122*2,110*2)).convert_alpha())
BossIdleImages1.append(pygame.transform.scale(pygame.image.load("Boss/1/tile002.png"),(122*2,110*2)).convert_alpha())
BossIdleImages1.append(pygame.transform.scale(pygame.image.load("Boss/1/tile003.png"),(122*2,110*2)).convert_alpha())
BossIdleImages1.append(pygame.transform.scale(pygame.image.load("Boss/1/tile004.png"),(122*2,110*2)).convert_alpha())
BossIdleImages1.append(pygame.transform.scale(pygame.image.load("Boss/1/tile005.png"),(122*2,110*2)).convert_alpha())
BossIdleImages1.append(pygame.transform.scale(pygame.image.load("Boss/1/tile006.png"),(122*2,110*2)).convert_alpha())
BossIdleImages1.append(pygame.transform.scale(pygame.image.load("Boss/1/tile007.png"),(122*2,110*2)).convert_alpha())
BossIdleImages1Left=[]
for image in BossIdleImages1:
    BossIdleImages1Left.append(pygame.transform.flip(image,True,False))
BossIdleImages2=[]
BossIdleImages2.append(pygame.transform.scale(pygame.image.load("Boss/2/tile000.png"),(87*2,110*2)).convert_alpha())
BossIdleImages2.append(pygame.transform.scale(pygame.image.load("Boss/2/tile002.png"),(87*2,110*2)).convert_alpha())
BossIdleImages2.append(pygame.transform.scale(pygame.image.load("Boss/2/tile002.png"),(87*2,110*2)).convert_alpha())
BossIdleImages2.append(pygame.transform.scale(pygame.image.load("Boss/2/tile003.png"),(87*2,110*2)).convert_alpha())
BossIdleImages2.append(pygame.transform.scale(pygame.image.load("Boss/2/tile004.png"),(87*2,110*2)).convert_alpha())
BossIdleImages2.append(pygame.transform.scale(pygame.image.load("Boss/2/tile005.png"),(87*2,110*2)).convert_alpha())
BossIdleImages2.append(pygame.transform.scale(pygame.image.load("Boss/2/tile006.png"),(87*2,110*2)).convert_alpha())
BossIdleImages2.append(pygame.transform.scale(pygame.image.load("Boss/2/tile007.png"),(87*2,110*2)).convert_alpha())
BossIdleImages2Left=[]
for image in BossIdleImages2:
    BossIdleImages2Left.append(pygame.transform.flip(image,True,False))
FireBallImagesLeft=[]
FireBallImagesRight=[]
FireBallImagesLeft.append(pygame.transform.rotate(pygame.transform.scale(pygame.image.load("FireBall/tile000.png"),(32,32)).convert_alpha(),-90))
FireBallImagesLeft.append(pygame.transform.rotate(pygame.transform.scale(pygame.image.load("FireBall/tile001.png"),(32,32)).convert_alpha(),-90))
FireBallImagesLeft.append(pygame.transform.rotate(pygame.transform.scale(pygame.image.load("FireBall/tile002.png"),(32,32)).convert_alpha(),-90))
FireBallImagesLeft.append(pygame.transform.rotate(pygame.transform.scale(pygame.image.load("FireBall/tile003.png"),(32,32)).convert_alpha(),-90))
for image in FireBallImagesLeft:
    FireBallImagesRight.append(pygame.transform.flip(image,True,False))
