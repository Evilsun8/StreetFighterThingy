import pygame
import spritesheet

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')

sprite_sheet_image = pygame.image.load('Platformer/images/fight.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

FPS = 30
Background = (50, 50, 50)
BLACK = (0, 0, 0)

# Warum sind die Spreadsheets so ungreade...
animation_list = []
animation_steps = [4, 5, 9, 3, 5, 7]
action = 0
last_update = pygame.time.get_ticks()
animation_cool_down = 150
frame = 0
step_counter = 0
scale = 2
x = 0
y = SCREEN_HEIGHT - (130*scale)

for animation in animation_steps:
	temp_img_list = []
	for _ in range(animation):
		temp_img_list.append(sprite_sheet.get_image(step_counter, 48, 120, scale, BLACK))
		step_counter += 1
	animation_list.append(temp_img_list)


running = True
while running:

	# ~Hintergrund~
	screen.fill(Background)

	# ZEIT Oooooo
	current_time = pygame.time.get_ticks()
	if current_time - last_update >= animation_cool_down:
		last_update = current_time
		frame += 1
		if frame >= len(animation_list[action]):
			frame = 0

	# Frame für jede Aciton
	screen.blit(animation_list[action][frame], (x, y))

	# Kolidieren mit dem Rand :D
	if x > SCREEN_WIDTH - (48*scale):
		x -= 10
		action = 0
		frame = 0
	if x < 0:
		x += 10
		action = 0
		frame = 0
	if y > SCREEN_HEIGHT - (120*scale):
		y -= 10
		action = 0
		frame = 0
	if y < 0:
		y += 10
		action = 3
		frame = 0

	# Movie Schmovie
	speed = 10
	if action == 1:
		x += speed
	elif action == 3:
		y += speed
	elif action == 4:
		x -= speed
	elif action == 5:
		y -= speed


	#Events go BRRRRRR
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				action = 0
				frame = 0
			elif event.key == pygame.K_RIGHT:
				action = 1
				frame = 0
				speed = 2
			elif event.key == pygame.K_LSHIFT:
				action = 2
				frame = 0
			elif event.key == pygame.K_DOWN:
				action = 3
				frame = 0
			elif event.key == pygame.K_LEFT:
				action = 4
				frame = 0
			elif event.key == pygame.K_UP:
				action = 5
				frame = 0
	pygame.display.update()
	clock = pygame.time.Clock()
	clock.tick(FPS)

pygame.quit()