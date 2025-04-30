from PIL import Image
import os
import pygame



def sort_images(folder, items_list):
    folder_contents = os.listdir(folder)
    for file in folder_contents:
        items_list.append(os.path.join(folder, file))
    items_list.sort()
	

def organize_items(folder, items_list):
    folder_path = os.path.abspath(folder)
    img_number = 1
	
    for filename in os.listdir(folder_path):
        img_path = os.path.join(folder_path, filename)
		
        if filename.startswith(folder) and filename.endswith(".jpg"):
            img_number += 1
        else:
            with Image.open(img_path) as img:
                converted_img = img.convert("RGB")

                new_filename = f"{folder}_{img_number:02}.jpg"
                new_path = os.path.join(folder_path, new_filename)

                converted_img.save(new_path, "JPEG")
            os.remove(img_path)
            img_number += 1
    sort_images(folder, items_list)


def paste_image(screen, item, location_x, location_y):
	image = pygame.image.load(item).convert()
	screen.blit(image, (location_x, location_y))


def run_program(screen, bg_tile, tops_list, bottoms_list, shoes_list):
    running = True
    while running: 
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                running = False
        screen.blit(bg_tile, (0,0))
        paste_image(screen, tops_list[1], 0, 0)
        pygame.display.flip()
    pygame.quit()


def main():
	pygame.display.set_caption("Cher's Outfit Generator")
	resolution = (1920, 1080)
	screen = pygame.display.set_mode(resolution)
	bg_tile = (pygame.image.load("background/background.png").convert())
	tops_list = []
	bottoms_list = []
	shoes_list = []
	organize_items('tops', tops_list)
	organize_items('bottoms', bottoms_list)
	organize_items('shoes', shoes_list)
	run_program(screen, bg_tile, tops_list, bottoms_list, shoes_list)
		

if __name__ == "__main__":
	main()
