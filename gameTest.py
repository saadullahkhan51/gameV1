#! python3
import pygame
import os
import cv2
import glob
import random
from spritesheet import SpriteSheet

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

unarmed_hero_sheet = pygame.image.load(r"Sprites\adventurer\adventurer-Sheet.png").convert() # 0-3 idle, 4-7 crouch, 8-13 run, 14-23 movingjump, hero is 50x37
hand_combat_sheet = pygame.image.load(r"Sprites\adventurer\adventurer-hand-combat-Sheet.png").convert()

unarmed_hero_sprites = SpriteSheet(unarmed_hero_sheet)
heroIdle = []
heroCrouch = []
heroRun = []
heroMovingJump = []
for i in range(4):
    frame = unarmed_hero_sprites.get_sheet(i, 0, 50, 37, 1, black) # picking from the first row manually 
    heroIdle.append(frame)
for i in range(4,8):
    frame = unarmed_hero_sprites.get_sheet(i, 0, 50, 37, 2, black) # picking from the first row manually 
    heroCrouch.append(frame)
for i in range(1,7):
    frame = unarmed_hero_sprites.get_sheet(i, 1, 50, 37, 2, black) # picking from the first row manually 
    heroRun.append(frame)
for i in range(7):
    frame = unarmed_hero_sprites.get_sheet(i, 2, 50, 37, 2, black) # picking from the first row manually 
    heroMovingJump.append(frame)
    j = 0
    if i==6:
        for j in range(3):
            frame = unarmed_hero_sprites.get_sheet(j, 3, 50, 37, 2, black)
            heroMovingJump.append(frame)
    

print(heroMovingJump)


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
                    win.blit(pygame.transform.flip(heroRun[int(self.walkCount//6)], 1, 0),(self.x, self.y))    # walkCount changes the index so the images line up with the framerate //3 is integer division
                    self.walkCount += 1
                elif self.right:
                    win.blit(pygame.transform.flip(heroRun[int(self.walkCount//6)], 0, 0),(self.x, self.y))
                    self.walkCount += 1
            #elif self.jump:
            elif self.jump:
                # play moving jump motion
                if self.toLeft:
                    win.blit(pygame.transform.flip(heroMovingJump[int(self.movJumpCount)], 1, 0),(self.x, self.y))    # walkCount changes the index so the images line up with the framerate //3 is integer division
                    self.movJumpCount += 0.5
                else:
                    win.blit(pygame.transform.flip(heroMovingJump[int(self.movJumpCount)], 0, 0),(self.x, self.y))
                    self.movJumpCount += 0.5

            else:
                self.idleCount += 0.5
                if self.toLeft:
                    win.blit(pygame.transform.flip(heroIdle[int(self.idleCount//4)], 1, 0),(self.x, self.y))
                else:
                    win.blit(pygame.transform.flip(heroIdle[int(self.idleCount//4)], 0, 0),(self.x, self.y))
            
        else:
            self.attackCount += 0.4
            win.blit(pygame.transform.flip(attack[int(self.attackCount)], 0, 0), (self.x, self.y))

        




class Enemy():
    def __init__(self):
        pass
    pass

### SKELETON CODE ######################
###idle####
skeleton_idle_image = pygame.image.load("Sprites\Monsters_Creatures_Fantasy\Skeleton\Idle.png").convert()
skeleton_idle_sprite = SpriteSheet(skeleton_idle_image)
skeletonIdle = []
for i in range(4):
    frame = skeleton_idle_sprite.get_image(i, 150, 150, 1, black)
    skeletonIdle.append(frame)
###########

####attack###
skeleton_attack_image = pygame.image.load("Sprites\Monsters_Creatures_Fantasy\Skeleton\Attack.png").convert()
skeleton_attack_sprite = SpriteSheet(skeleton_attack_image)
skeletonAttack = []
for i in range(8):
    frame = skeleton_attack_sprite.get_image(i, 150, 150, 1, black)
    skeletonAttack.append(frame)
###########

## flip() so we dont need left right sprites

class Skeleton(Enemy):
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
        self.left = False
        self.right = False
        self.walkCount = 0
        self.idleCount = 0
        self.attackCount = 0
        self.idle = True
        self.toLeft = False
        self.toRight = False
        self.attack = False

    def draw(self, win):
        if self.idleCount + 1 >=16:
            self.idleCount = 0
        if self.attackCount + 1 >=8:
            self.attack = False
            self.attackCount = 0

        if self.attack:
            self.attackCount += 0.4
            win.blit(pygame.transform.flip(skeletonAttack[int(self.attackCount)], 0, 0), (self.x, self.y))
        else:
            self.idleCount += 0.5
            win.blit(pygame.transform.flip(skeletonIdle[int(self.idleCount//4)], 0, 0),(self.x, self.y))

            

#########################################

#Sprite movement
hero = Player(40, 540 - offset, 64 , 64)
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
    win.blit(heroMovingJump[7], (100, 100))
    win.blit(heroCrouch[1], (150, 100))
    
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