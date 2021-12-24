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
        self.bowAttack = False
        self.bowCount = 0
        self.dash = False
        self.hitbox = (self.x+15, self.y, self.width-30, self.height)

        self.unarmed_hero_sheet = pygame.image.load(r"Sprites\adventurer\adventurer-Sheet.png").convert() # 0-3 idle, 4-7 crouch, 8-13 run, 14-23 movingjump, hero is 50x37
        self.hand_combat_sheet = pygame.image.load(r"Sprites\adventurer\adventurer-hand-combat-Sheet.png").convert()

        # Movement sprites
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
        
        # Attack sprites
        self.hand_combat_sprites = SpriteSheet(self.hand_combat_sheet)
        self.attackFrame, self.attack2Frame = [], []
        for j in range(2):
            for i in range(7):
                frame = self.hand_combat_sprites.get_sheet(i, j, 50, 37, 2, black) # picking from the first row manually 
                self.attackFrame.append(frame)

        # Bow sprites
        self.bow_sheet = pygame.image.load(r"Sprites\adventurer\adventurer-bow-Sheet.png").convert()
        self.bow_sprites = SpriteSheet(self.bow_sheet)
        self.bowFrame = []
        for j in range(3):
            for i in range(4):
                if len(self.bowFrame) == 9:
                    break
                frame = self.bow_sprites.get_sheet(i, j, 50, 37, 2, black) # picking from the first row manually 
                self.bowFrame.append(frame)
                



    def draw(self, win):
        if self.walkCount + 1 >= 36:
            self.walkCount = 0
        if self.idleCount + 1 >= 16:
            self.idleCount = 0
        if self.attackCount + 1 >= 14:
            self.attack = False
            self.attackCount = 0
        if self.bowCount + 1 >= 9:
            self.bowAttack = False
            self.bowCount = 0
        if self.movJumpCount + 1 >= 10 or not self.jump:
            self.movJumpCount = 0


        # Might need to rewrite this logic
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
            elif self.bowAttack:
                if self.toLeft:
                    win.blit(pygame.transform.flip(self.bowFrame[int(self.bowCount)], 1, 0), (self.x, self.y))
                    self.bowCount += 0.5
                else:
                    win.blit(pygame.transform.flip(self.bowFrame[int(self.bowCount)], 0, 0), (self.x, self.y))
                    self.bowCount += 0.5

            else:
                self.idleCount += 0.5
                if self.toLeft:
                    win.blit(pygame.transform.flip(self.heroIdle[int(self.idleCount//4)], 1, 0),(self.x, self.y))
                else:
                    win.blit(pygame.transform.flip(self.heroIdle[int(self.idleCount//4)], 0, 0),(self.x, self.y))
            
        else:
            if self.toLeft:
                win.blit(pygame.transform.flip(self.attackFrame[int(self.attackCount)], 1, 0), (self.x, self.y))
                self.attackCount += 0.4
            else:
                win.blit(pygame.transform.flip(self.attackFrame[int(self.attackCount)], 0, 0), (self.x, self.y))
                self.attackCount += 0.4
        self.hitbox = (self.x+15, self.y, self.width-30, self.height)
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
