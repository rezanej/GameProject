import os

import pygame
from Setting import *
from os import remove
class OptionMenu():
    PlayMusic = False
    def __init__(self,display,levelTrue,level):
        self.display=display
        self.levelTrue=levelTrue
        self.level=level
        self.background=MenuBackground
        self.backgroundRect=self.background.get_rect()
        self.pauseText=MenuFont.render("Options",True,(40,56,32))
        self.pauseTextRect=self.pauseText.get_rect(center=(WindowWidth//2,WindowHeight//2 -200))
        self.selectedButton=1
        self.buttonOffset=-80
        self.changeImage=False
        self.button1=ButtonImages[1]
        self.button1Rect=self.button1.get_rect(center=(WindowWidth//2,WindowHeight//2+self.buttonOffset))
        self.button2=ButtonImages[1]
        self.button2Rect=self.button2.get_rect(center=(WindowWidth//2,WindowHeight//2+self.buttonOffset+100))
        self.button3=ButtonImages[1]
        self.button3Rect=self.button3.get_rect(center=(WindowWidth//2,WindowHeight//2+self.buttonOffset+120))
        self.resumeText=MenuButtonFont.render("Music : ON",True,MenuButtonTextColor)
        self.resumeTextRect=self.resumeText.get_rect(center=(WindowWidth//2,WindowHeight//2+self.buttonOffset))
        self.mainMenuText=MenuButtonFont.render("Reset Save",True,MenuButtonTextColor)
        self.mainMenuTextRect=self.mainMenuText.get_rect(center=(WindowWidth//2,WindowHeight//2+100+self.buttonOffset))
        self.optionText=MenuButtonFont.render("Back",True,MenuButtonTextColor)
        self.optionTextRect=self.optionText.get_rect(center=(WindowWidth//2,WindowHeight//2+200+self.buttonOffset))
        self.lastMenu=0

    def blit(self):
        self.display.blit(self.background,self.backgroundRect)
        self.display.blit(self.pauseText,self.pauseTextRect)
        self.display.blit(self.button1,self.button1Rect)
        self.display.blit(self.resumeText,self.resumeTextRect)
        self.display.blit(self.button2, self.button2Rect)
        self.display.blit(self.mainMenuText,self.mainMenuTextRect)
        self.display.blit(self.button3, self.button3Rect)
        self.display.blit(self.optionText,self.optionTextRect)
    def menuLoop(self,events,lastMenu):
        self.events=events
        self.lastMenu=lastMenu
        for event in self.events:

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_DOWN:
                    self.selectedButton+=1
                elif event.key==pygame.K_UP:
                    if self.selectedButton==1:
                        self.selectedButton=3
                    else:
                        self.selectedButton-=1
                if event.key==pygame.K_RETURN:
                    if self.selectedButton==1:
                        if OptionMenu.PlayMusic==True:
                            pygame.mixer.music.pause()
                            with open("save.txt", "r") as save:
                                lines = save.readlines()
                            with open("save.txt", "w") as f:
                                for i in range(len(lines)-1):
                                    f.writelines(lines[i].strip("\n")+"\n")
                                f.writelines("0")
                            OptionMenu.PlayMusic = False
                        elif OptionMenu.PlayMusic==False:
                            pygame.mixer.music.load("Music/NinjaManFightVer(remixAgain1).mp3")
                            pygame.mixer.music.play()
                            with open("save.txt", "r") as save:
                                lines = save.readlines()
                            with open("save.txt", "w") as f:
                                for i in range(len(lines)-1):
                                    f.writelines(lines[i].strip("\n")+"\n")
                                f.writelines("1")
                            OptionMenu.PlayMusic=True

                    if self.selectedButton==2:
                        remove("save.txt")
                        self.level.reset()
                        self.levelTrue[0] = 0
                        self.levelTrue[6] = 0
                        self.levelTrue[7] = 0
                    if self.selectedButton==3:
                        if self.lastMenu==0:
                            self.levelTrue[0]=0
                            self.levelTrue[6] = 0
                        else :
                            self.levelTrue[1]=1
                            self.levelTrue[7]=0



        if self.selectedButton==1:
            self.button1Rect = self.button1.get_rect(center=(WindowWidth // 2, WindowHeight // 2+self.buttonOffset))
            self.button2Rect = self.button2.get_rect(center=(WindowWidth // 2, WindowHeight // 2 +self.buttonOffset+100))
            self.button3Rect = self.button3.get_rect(center=(WindowWidth // 2, WindowHeight // 2 +self.buttonOffset+200))
            self.button1=ButtonImages[0]
            self.button2=ButtonImages[1]
            self.button3=ButtonImages[1]
        elif self.selectedButton==2:
            self.button1Rect = self.button1.get_rect(center=(WindowWidth // 2, WindowHeight // 2 + self.buttonOffset))
            self.button2Rect = self.button2.get_rect(
                center=(WindowWidth // 2, WindowHeight // 2 + self.buttonOffset + 100))
            self.button3Rect = self.button3.get_rect(
                center=(WindowWidth // 2, WindowHeight // 2 + self.buttonOffset + 200))
            self.button2 = ButtonImages[0]
            self.button1 = ButtonImages[1]
            self.button3 = ButtonImages[1]
        elif self.selectedButton==3:
            self.button1Rect = self.button1.get_rect(center=(WindowWidth // 2, WindowHeight // 2 + self.buttonOffset))
            self.button2Rect = self.button2.get_rect(
                center=(WindowWidth // 2, WindowHeight // 2 + self.buttonOffset + 100))
            self.button3Rect = self.button3.get_rect(
                center=(WindowWidth // 2, WindowHeight // 2 + self.buttonOffset + 200))
            self.button3 = ButtonImages[0]
            self.button1 = ButtonImages[1]
            self.button2 = ButtonImages[1]
        else:
            self.selectedButton=1


        self.blit()
        return True