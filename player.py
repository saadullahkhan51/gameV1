import pygame
import os
import glob
import random
from spritesheet import SpriteSheet


black = (0,0,0)

#Positioning of block
class Player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.val = 5
        self.jump = False
        self.jumpHeight = 10
        self.jumpCount = self.jumpHeight
        self.movJumpCount = 0
        self.left = False
        self.right = False
        self.walkCount = 0
        self.idleCount = 0
        self.attackCount = 0
        self.idle = True
        self.toLeft = False
        self.toRight = False
        self.attack = False

        self.unarmed_hero_sheet = pygame.image.load(r"Sprites\adventurer\adventurer-Sheet.png").convert() # 0-3 idle, 4-7 crouch, 8-13 run, 14-23 movingjump, hero is 50x37
        self.hand_combat_sheet = pygame.image.load(r"Sprites\adventurer\adventurer-hand-combat-Sheet.png").convert()

        self.unarmed_hero_sprites = SpriteSheet(self.unarmed_hero_sheet)
        self.heroIdle = []
        self.heroCrouch = []
        self.heroRun = []
        self.heroMovingJump = []
        for i in range(4):
            frame = self.unarmed_hero_sprites.get_sheet(i, 0, 50, 37, 1, black) # picking from the first row manually 
            self.heroIdle.append(frame)
        for i in range(4,8):
            frame = self.unarmed_hero_sprites.get_sheet(i, 0, 50, 37, 2, black) # picking from the first row manually 
            self.heroCrouch.append(frame)
        for i in range(1,7):
            frame = self.unarmed_hero_sprites.get_sheet(i, 1, 50, 37, 2, black) # picking from the first row manually 
            self.heroRun.append(frame)
        for i in range(7):
            frame = self.unarmed_hero_sprites.get_sheet(i, 2, 50, 37, 2, black) # picking from the first row manually 
            self.heroMovingJump.append(frame)
            j = 0
            if i==6:
                for j in range(3):
                    frame = self.unarmed_hero_sprites.get_sheet(j, 3, 50, 37, 2, black)
                    self.heroMovingJump.append(frame)
        
    def draw(self, win):
        if self.walkCount + 1 >= 36:
            self.walkCount = 0
        if self.idleCount + 1 >=16:
            self.idleCount = 0
        if self.attackCount + 1 >=9:
            self.attack = False
            self.attackCount = 0
        if self.movJumpCount + 1 >= 10 or not self.jump:
            self.movJumpCount = 0

        if not(self.attack):
            if not self.idle and not self.jump:
                if self.left:
                    win.blit(pygame.transform.flip(self.heroRun[int(self.walkCount//6)], 1, 0),(self.x, self.y))    # walkCount changes the index so the images line up with the framerate //3 is integer division
                    self.walkCount += 1
                elif self.right:
                    win.blit(pygame.transform.flip(self.heroRun[int(self.walkCount//6)], 0, 0),(self.x, self.y))
                    self.walkCount += 1
            #elif self.jump:
            elif self.jump:
                # play moving jump motion
                if self.toLeft:
                    win.blit(pygame.transform.flip(self.heroMovingJump[int(self.movJumpCount)], 1, 0),(self.x, self.y))    # walkCount changes the index so the images line up with the framerate //3 is integer division
                    self.movJumpCount += 0.5
                else:
                    win.blit(pygame.transform.flip(self.heroMovingJump[int(self.movJumpCount)], 0, 0),(self.x, self.y))
                    self.movJumpCount += 0.5

            else:
                self.idleCount += 0.5
                if self.toLeft:
                    win.blit(pygame.transform.flip(self.heroIdle[int(self.idleCount//4)], 1, 0),(self.x, self.y))
                else:
                    win.blit(pygame.transform.flip(self.heroIdle[int(self.idleCount//4)], 0, 0),(self.x, self.y))
            
        else:
            self.attackCount += 0.4
            #win.blit(pygame.transform.flip(attack[int(self.attackCount)], 0, 0), (self.x, self.y))
