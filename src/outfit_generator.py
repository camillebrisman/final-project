from PIL import Image
import os
import pygame


def sort_items(folder):
    folder_path = os.path.abspath(folder)
    img_number = 1
	
    for filename in os.listdir(folder_path):
        img_path = os.path.join(folder_path, filename)
		
        with Image.open(img_path) as img:
            converted_img = img.convert("RGB")

            new_filename = f"{folder}_{img_number}.jpg"
            new_path = os.path.join(folder_path, new_filename)

            converted_img.save(new_path, "JPEG")
            os.remove(img_path)
        img_number += 1


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
	sort_items('tops')
	run_program(screen, bg_tile)
		

if __name__ == "__main__":
	main()
