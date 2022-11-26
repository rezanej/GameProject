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
BackgroundImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/BG/BG.png"),(64*20,640)).convert_alpha())
PlayerImage=pygame.transform.scale(pygame.image.load("PlayerImages/Idle__000.png"),(232/7,439/7)).convert_alpha()
DirtImages=[]
DirtImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/Tiles/5.png"),(64,64)).convert_alpha())
DirtImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/Tiles/8.png"),(64,64)))
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
ObjectImages=[]
ObjectImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/Object/Bush (1).png"),(133,65)).convert_alpha())
ObjectImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/Object/Bush (2).png"),(133,65)).convert_alpha())
# ObjectImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/Object/Crate.png"),(77,77)).convert_alpha())
ObjectImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/Object/Mushroom_1.png"),(49,41)).convert_alpha())
ObjectImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/Object/Mushroom_2.png"),(49,41)).convert_alpha())
ObjectImages.append(pygame.transform.scale(pygame.image.load("Level1Assets/Object/Stone.png"),(90,54)).convert_alpha())
Level1TileMap="00000000000000000000000000000000000000000000000000n" \
              "bB000000000000000000000000000000000000000000000000n" \
              "bB0000000B0000000000000000000B00000000000000000000n" \
              "bB0000000B0000000000000000000B00000000000000000000n" \
              "bB0000000B0000000000000000000B00000000000000000000n" \
              "bBT0CDCCTB00000pP00000NcccTT0B00000000000000000000n" \
              "111111111100000110011111111111000000hP00000000000n" \
              "ddddddddh000T00000000010t01000010t0011100000000000n" \
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
              "ddddddddddddddddddddddddddddddddddddddddn" \
              "ddddddddddddddddddddddddddddddddddddddddn"
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
