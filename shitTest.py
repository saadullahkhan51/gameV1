import pygame
from spritesheet import SpriteSheet

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')

sprite_sheet_image = pygame.image.load("Sprites\Monsters_Creatures_Fantasy\Skeleton\Idle.png").convert()
image_width = sprite_sheet_image.get_width()
print(image_width)
sprite_sheet = SpriteSheet(sprite_sheet_image)

unarmed_hero_sheet = pygame.image.load("Sprites\\adventurer\\adventurer-Sheet.png").convert()
hero = SpriteSheet(unarmed_hero_sheet)

BG = (50, 50, 50)
BLACK = (0, 0, 0)
white = (100, 100, 100)

frame_0 = sprite_sheet.get_image(0, 150, 150, 1, BLACK)

heroF = hero.get_sheet(0, 8, 37, 37, 3, BLACK)
### Skeleton idle frames 
frames = []
for i in range(4):
    frame = sprite_sheet.get_image(i, 150, 150, 1, BLACK)
    frames.append(frame)
###

flipped = pygame.transform.flip(frame_0, 1, 0)
#frame_0.set_colorkey(BLACK)
run = True
while run:

	#update background
	screen.fill(BG)

	#show frame image
	screen.blit(heroF, (0, 0))

	#event handler
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()