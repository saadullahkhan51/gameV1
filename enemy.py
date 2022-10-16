import pygame
import os
import glob
import random
from spritesheet import SpriteSheet

black = (0,0,0)

class Enemy():
    def __init__(self):
        pass
    pass

## flip() so we dont need left right sprites

class Skeleton(Enemy):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.val = 5
        self.jump = False
        self.jumpHeight = 10
        self.jumpCount = self.jumpHeight
        self.left = False
        self.right = False
        self.walkCount = 0
        self.idleCount = 0
        self.attackCount = 0
        self.idle = True
        self.toLeft = False
        self.toRight = False
        self.attack = False
        self.path = [self.x, end]
        self.hitbox = (self.x, self.y+50, 30, 60)

        ### SKELETON CODE ######################
        black = (0,0,0)
        ###idle####
        self.skeleton_idle_image = pygame.image.load("Sprites\Monsters_Creatures_Fantasy\Skeleton\Idle.png").convert()
        self.skeleton_idle_sprite = SpriteSheet(self.skeleton_idle_image)
        self.skeletonIdle = []
        for i in range(4):
            frame = self.skeleton_idle_sprite.get_image(i, 150, 150, 1, black)
            self.skeletonIdle.append(frame)
        ###########

        ####attack###
        self.skeleton_attack_image = pygame.image.load("Sprites\Monsters_Creatures_Fantasy\Skeleton\Attack.png").convert()
        self.skeleton_attack_sprite = SpriteSheet(self.skeleton_attack_image)
        self.skeletonAttack = []
        for i in range(8):
            frame = self.skeleton_attack_sprite.get_image(i, 150, 150, 1, black)
            self.skeletonAttack.append(frame)
        ###########

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def draw(self, win):
        if self.idleCount + 1 >=16:
            self.idleCount = 0
        if self.attackCount + 1 >=8:
            self.attack = False
            self.attackCount = 0

        if self.attack:
            self.attackCount += 0.4
            win.blit(pygame.transform.flip(self.skeletonAttack[int(self.attackCount)], 0, 0), (self.x, self.y))
        else:
            self.idleCount += 0.5
            win.blit(pygame.transform.flip(self.skeletonIdle[int(self.idleCount//4)], 0, 0),(self.x, self.y))
        self.hitbox = (self.x+60, self.y+40, 40, 60)
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
    
    def hit(self):
        pass
