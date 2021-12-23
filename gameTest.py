#! python3
import pygame
import os
import cv2
import glob
import random
from spritesheet import SpriteSheet
import player
from enemy import Skeleton

pygame.init()
#os.chdir(r"C:\Users\Saadullah\Documents\PythonScripts")
spritePath = ("Sprites\Individual Sprites")
runPath = ("Sprites\Run")
attackPath = ("Sprites\Spear")

images = os.listdir(spritePath)
runSprites = os.listdir(runPath)
attackSprites = os.listdir(attackPath)

#Loading the screen and Images
win_width= 800
win_height= 600
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("PRACTICE GAME!!")
#BASE = pygame.image.load(os.path.join("imgs", "base.png"))
#BG = pygame.image.load(os.path.join("imgs", "bg.png"))
#need to implement OOP to the BG
env = pygame.image.load(os.path.join("Sprites", "environment1.png"))
env_x = 0
env_vel = 3
offset = 0

#walkRight = [pygame.image.load(os.path.join("imgs\Game", "R1.png")),pygame.image.load(os.path.join("imgs\Game", "R2.png")),pygame.image.load(os.path.join("imgs\Game", "R3.png")),pygame.image.load(os.path.join("imgs\Game", "R4.png")),pygame.image.load(os.path.join("imgs\Game", "R5.png")),pygame.image.load(os.path.join("imgs\Game", "R6.png")),pygame.image.load(os.path.join("imgs\Game", "R7.png")),pygame.image.load(os.path.join("imgs\Game", "R8.png")),pygame.image.load(os.path.join("imgs\Game", "R9.png"))]
#character = pygame.image.load(os.path.join("imgs\Game", "Standing.png"))
#walkLeft = [pygame.image.load(os.path.join("imgs\Game", "L1.png")),pygame.image.load(os.path.join("imgs\Game", "L2.png")),pygame.image.load(os.path.join("imgs\Game", "L3.png")),pygame.image.load(os.path.join("imgs\Game", "L4.png")),pygame.image.load(os.path.join("imgs\Game", "L5.png")),pygame.image.load(os.path.join("imgs\Game", "L6.png")),pygame.image.load(os.path.join("imgs\Game", "L7.png")),pygame.image.load(os.path.join("imgs\Game", "L8.png")),pygame.image.load(os.path.join("imgs\Game", "L9.png"))]
black= (0,0,0)

### for hero ###
idleLeft = [pygame.image.load(os.path.join(spritePath, images[53])),pygame.image.load(os.path.join(spritePath, images[54])),pygame.image.load(os.path.join(spritePath, images[55])),pygame.image.load(os.path.join(spritePath, images[53])),pygame.image.load(os.path.join(spritePath, images[54])),pygame.image.load(os.path.join(spritePath, images[55])),pygame.image.load(os.path.join(spritePath, images[53])),pygame.image.load(os.path.join(spritePath, images[54])),pygame.image.load(os.path.join(spritePath, images[55]))]
idleRight = [pygame.image.load(os.path.join(spritePath, images[49])),pygame.image.load(os.path.join(spritePath, images[50])),pygame.image.load(os.path.join(spritePath, images[51])),pygame.image.load(os.path.join(spritePath, images[49])),pygame.image.load(os.path.join(spritePath, images[50])),pygame.image.load(os.path.join(spritePath, images[51])),pygame.image.load(os.path.join(spritePath, images[49])),pygame.image.load(os.path.join(spritePath, images[50])),pygame.image.load(os.path.join(spritePath, images[51]))]
walkRight2 = [pygame.image.load(os.path.join(runPath, runSprites[0])), pygame.image.load(os.path.join(runPath, runSprites[1])), pygame.image.load(os.path.join(runPath, runSprites[2])),pygame.image.load(os.path.join(runPath, runSprites[3])),pygame.image.load(os.path.join(runPath, runSprites[4])),pygame.image.load(os.path.join(runPath, runSprites[5])),pygame.image.load(os.path.join(runPath, runSprites[0])),pygame.image.load(os.path.join(runPath, runSprites[1])),pygame.image.load(os.path.join(runPath, runSprites[2]))]
walkLeft2 = [pygame.image.load(os.path.join(runPath, runSprites[6])), pygame.image.load(os.path.join(runPath, runSprites[7])), pygame.image.load(os.path.join(runPath, runSprites[8])),pygame.image.load(os.path.join(runPath, runSprites[9])), pygame.image.load(os.path.join(runPath, runSprites[10])), pygame.image.load(os.path.join(runPath, runSprites[11])), pygame.image.load(os.path.join(runPath, runSprites[6])), pygame.image.load(os.path.join(runPath, runSprites[7])), pygame.image.load(os.path.join(runPath, runSprites[8]))]
attack  = [pygame.image.load(os.path.join(attackPath, attackSprites[0])),pygame.image.load(os.path.join(attackPath, attackSprites[1])),pygame.image.load(os.path.join(attackPath, attackSprites[2])),pygame.image.load(os.path.join(attackPath, attackSprites[3])),pygame.image.load(os.path.join(attackPath, attackSprites[4])),pygame.image.load(os.path.join(attackPath, attackSprites[5])),pygame.image.load(os.path.join(attackPath, attackSprites[6])),pygame.image.load(os.path.join(attackPath, attackSprites[7])),pygame.image.load(os.path.join(attackPath, attackSprites[8])),pygame.image.load(os.path.join(attackPath, attackSprites[9]))]
###


#--------------------------Everything above this is cursed code-------------------------------#

## PLAYER CODE WAS HERE

## ENEMY CODE WAS HERE
            

#########################################

#Sprite movement
hero = player.Player(40, 540 - offset, 64 , 64)
skeleton = Skeleton(80, 450, 150, 150)
velLabel = pygame.font.Font(None, 50)
velDisplay = velLabel.render(str(hero.vel), 1, (255,255,0))
#hero2 = player(30, 424 , 50 , 37)
FPS = pygame.time.Clock()

def drawingGameWin():
    # Drawing the background
    #win.blit(BG,(0,0))
    #win.blit(BG,(288,0))
    #win.blit(BG,(576,0))
    #win.blit(BASE,(0,488))
    #win.blit(BASE,(336,488))
    #win.blit(BASE,(336+336,488))
    win.blit(env,(env_x,0))
    skeleton.draw(win)
    hero.draw(win)
    
    win.blit(velDisplay,(10,10))
    pygame.display.update()
    #win.blit(hero,(hero.x -cameraX,hero.y -cameraY))
    pygame.display.flip()

run= True
while run:

    FPS.tick(27)
    drawingGameWin()
    win.blit(velDisplay,(10,10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run= False
    #hero.attack = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] and hero.x < win_width - hero.width:
        hero.x += hero.vel
        hero.right = True
        hero.left = False
        hero.idle = False
        hero.toRight = True
        hero.toLeft = False
        #shift_color_x += 1
    elif keys[pygame.K_a] and hero.x > 0:
        hero.x -= hero.vel
        hero.right = False
        hero.left = True
        hero.idle = False
        hero.toLeft = True
        hero.toRight = False
    else:
        hero.right = False
        hero.left = False
        hero.walkCount = 0
        hero.idle = True

    if keys[pygame.K_SPACE]:
        hero.attack = True
        skeleton.attack = True
        #shift_color_x -= 0.5
    
    if not(hero.jump):
        '''if keys[pygame.K_s] and y < 488 - width:
                y += vel
                #shift_color_y -= 0.5
        if keys[pygame.K_w] and y > 0:
            y -= vel
            #shift_color_y += 1'''
        if keys[pygame.K_w]:
            hero.jump = True
            hero.right = False
            hero.left = False
            hero.walkCount = 0
        direction = 1
    else:
        if hero.jumpCount >= -hero.jumpHeight:
            if hero.jumpCount < 0:
                direction = -1
            hero.y -= (hero.jumpCount**2)*0.3* direction
            hero.jumpCount -= 1
        else:
            hero.jump = False
            hero.jumpCount = hero.jumpHeight

    if abs(env_x) < 650 and hero.x > 400 and hero.right:
        env_x -= env_vel
        hero.vel = -2
    else:
        hero.vel = hero.val
    if abs(env_x) > 0 and hero.x < 400 and hero.left:
        env_x += env_vel
        hero.vel = 2
    else:
        hero.vel = hero.val
    #hero.vel = hero.val

pygame.quit()