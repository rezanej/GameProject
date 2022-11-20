import pygame
from Setting import *
from Level import Level
class PauseMenu():
    def __init__(self,display,levelTrue):
        self.display=display
        self.levelTrue=levelTrue
        self.background=MenuBackground
        self.backgroundRect=self.background.get_rect()
        self.pauseText=MenuFont.render("Paused",True,(40,56,32))
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
        self.button4=ButtonImages[1]
        self.button4Rect=self.button4.get_rect(center=(WindowWidth//2,WindowHeight//2+self.buttonOffset+220))
        self.resumeText=MenuButtonFont.render("Resume",True,MenuButtonTextColor)
        self.resumeTextRect=self.resumeText.get_rect(center=(WindowWidth//2,WindowHeight//2+self.buttonOffset))
        self.mainMenuText=MenuButtonFont.render("Main Menu",True,MenuButtonTextColor)
        self.mainMenuTextRect=self.mainMenuText.get_rect(center=(WindowWidth//2,WindowHeight//2+100+self.buttonOffset))
        self.optionText=MenuButtonFont.render("Options",True,MenuButtonTextColor)
        self.optionTextRect=self.optionText.get_rect(center=(WindowWidth//2,WindowHeight//2+200+self.buttonOffset))
        self.exitText=MenuButtonFont.render("Exit",True,MenuButtonTextColor)
        self.exitTextRect=self.exitText.get_rect(center=(WindowWidth//2,WindowHeight//2+300+self.buttonOffset))
    def blit(self):
        self.display.blit(self.background,self.backgroundRect)
        self.display.blit(self.pauseText,self.pauseTextRect)
        self.display.blit(self.button1,self.button1Rect)
        self.display.blit(self.resumeText,self.resumeTextRect)
        self.display.blit(self.button2, self.button2Rect)
        self.display.blit(self.mainMenuText,self.mainMenuTextRect)
        self.display.blit(self.button3, self.button3Rect)
        self.display.blit(self.optionText,self.optionTextRect)
        self.display.blit(self.button4,self.button4Rect)
        self.display.blit(self.exitText,self.exitTextRect)
    def menuLoop(self,events):

        for event in events:

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_DOWN:
                    self.selectedButton+=1
                elif event.key==pygame.K_UP:
                    if self.selectedButton==1:
                        self.selectedButton=4
                    else:
                        self.selectedButton-=1
                if event.key==pygame.K_RETURN:
                    if self.selectedButton==1:
                        self.levelTrue[1]=0
                    if self.selectedButton==2:
                        self.levelTrue[1]=0
                        self.levelTrue[0]=0
                        self.levelTrue[2]=1

                    if self.selectedButton==4:
                        return False


        if self.selectedButton==1:
            self.button1Rect = self.button1.get_rect(center=(WindowWidth // 2, WindowHeight // 2+self.buttonOffset))
            self.button2Rect = self.button2.get_rect(center=(WindowWidth // 2, WindowHeight // 2 +self.buttonOffset+100))
            self.button3Rect = self.button3.get_rect(center=(WindowWidth // 2, WindowHeight // 2 +self.buttonOffset+200))
            self.button4Rect = self.button4.get_rect(center=(WindowWidth // 2, WindowHeight // 2 +self.buttonOffset+300))
            self.button1=ButtonImages[0]
            self.button2=ButtonImages[1]
            self.button3=ButtonImages[1]
            self.button4=ButtonImages[1]
        elif self.selectedButton==2:
            self.button1Rect = self.button1.get_rect(center=(WindowWidth // 2, WindowHeight // 2 + self.buttonOffset))
            self.button2Rect = self.button2.get_rect(
                center=(WindowWidth // 2, WindowHeight // 2 + self.buttonOffset + 100))
            self.button3Rect = self.button3.get_rect(
                center=(WindowWidth // 2, WindowHeight // 2 + self.buttonOffset + 200))
            self.button4Rect = self.button4.get_rect(
                center=(WindowWidth // 2, WindowHeight // 2 + self.buttonOffset + 300))
            self.button2 = ButtonImages[0]
            self.button1 = ButtonImages[1]
            self.button3 = ButtonImages[1]
            self.button4 = ButtonImages[1]
        elif self.selectedButton==3:
            self.button1Rect = self.button1.get_rect(center=(WindowWidth // 2, WindowHeight // 2 + self.buttonOffset))
            self.button2Rect = self.button2.get_rect(
                center=(WindowWidth // 2, WindowHeight // 2 + self.buttonOffset + 100))
            self.button3Rect = self.button3.get_rect(
                center=(WindowWidth // 2, WindowHeight // 2 + self.buttonOffset + 200))
            self.button4Rect = self.button4.get_rect(
                center=(WindowWidth // 2, WindowHeight // 2 + self.buttonOffset + 300))
            self.button3 = ButtonImages[0]
            self.button1 = ButtonImages[1]
            self.button2 = ButtonImages[1]
            self.button4 = ButtonImages[1]
        elif self.selectedButton==4:
            self.button1Rect = self.button1.get_rect(center=(WindowWidth // 2, WindowHeight // 2 + self.buttonOffset))
            self.button2Rect = self.button2.get_rect(
                center=(WindowWidth // 2, WindowHeight // 2 + self.buttonOffset + 100))
            self.button3Rect = self.button3.get_rect(
                center=(WindowWidth // 2, WindowHeight // 2 + self.buttonOffset + 200))
            self.button4Rect = self.button4.get_rect(
                center=(WindowWidth // 2, WindowHeight // 2 + self.buttonOffset + 300))
            self.button4 = ButtonImages[0]
            self.button1 = ButtonImages[1]
            self.button2 = ButtonImages[1]
            self.button3 = ButtonImages[1]
        else:
            self.selectedButton=1


        self.blit()
        return True