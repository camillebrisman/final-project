import pygame


def run_program(screen, bg_tile):
	running = True
	while running: 
		for event in pygame.event.get():
			keys = pygame.key.get_pressed()
			if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
				running = False
		screen.blit(bg_tile, (0,0))
		pygame.display.flip()
	pygame.quit()


def main():
	pygame.display.set_caption("Cher's Outfit Generator")
	resolution = (1920, 1080)
	screen = pygame.display.set_mode(resolution)
	bg_tile = (pygame.image.load("background/background.png").convert())
	run_program(screen, bg_tile)
		

if __name__ == "__main__":
	main()
