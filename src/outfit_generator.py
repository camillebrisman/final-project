from PIL import Image
import os
import pygame


def sort_images(folder, items_list):
    folder_contents = os.listdir(folder)
    for file in folder_contents:
        items_list.append(os.path.join(folder, file))
    items_list.sort()
	

def organize_items(folder, items_list, height):
    folder_path = os.path.abspath(folder)
    img_number = 1
	
    for filename in os.listdir(folder_path):
        img_path = os.path.join(folder_path, filename)
		
        if filename.startswith(folder) and filename.endswith(".jpg"):
            img_number += 1
        else:
            with Image.open(img_path) as img:
                converted_img = img.convert("RGB")
                ratio = img.width / img.height
                width = int(ratio * height)
                converted_img = converted_img.resize((width, height))

                new_filename = f"{folder}_{img_number:02}.jpg"
                new_path = os.path.join(folder_path, new_filename)

                converted_img.save(new_path, "JPEG")
            os.remove(img_path)
            img_number += 1
    sort_images(folder, items_list)


def paste_image(screen, item, location_x, location_y, items_index):
    image = pygame.image.load(item).convert_alpha()
    x = (1920 - image.get_width()) // 2
    if items_index == 0:
        screen.blit(image, (x, location_y))
    if items_index == 1:
        screen.blit(image, (location_x, location_y))
        return pygame.Rect(location_x, location_y, image.get_width(), image.get_height())


def paste_background(screen, items_index):
    buttons = {}

    save_image = "background/save_group.png"
    right_arrow = "background/right_arrow.png"
    left_arrow = "background/left_arrow.png"
    title_icon = "background/title_icon.png"
    randomize_group = "background/randomize_group.png"

    paste_image(screen, save_image, 0, (500), items_index)
    buttons['tops_arrow_r'] = paste_image(screen, right_arrow, 
                                          1150, 60, items_index)
    buttons['bottoms_arrow_r'] = paste_image(screen, right_arrow, 
                                             1150, 400, items_index)
    buttons['shoes_arrow_r'] = paste_image(screen, right_arrow, 
                                           1150, 740, items_index)
    buttons['tops_arrow_l'] = paste_image(screen, left_arrow, 
                                          550, 60, items_index)
    buttons['bottoms_arrow_l'] = paste_image(screen, left_arrow, 
                                             550, 400, items_index)
    buttons['shoes_arrow_l'] = paste_image(screen, left_arrow, 
                                           550, 740, items_index)
    paste_image(screen, title_icon, 0, 0, items_index)
    paste_image(screen, randomize_group, 1400, 325, items_index)

    return buttons


def paste_clothes(screen, tops_list, bottoms_list, shoes_list, items_index):
    paste_image(screen, tops_list, 0, 60, items_index)
    paste_image(screen, bottoms_list, 0,  400, items_index)
    paste_image(screen, shoes_list, 0, 740, items_index)


def load_screen(screen, bg_tile, tops_list, tops_index, bottoms_list, bottoms_index, 
                      shoes_list, shoes_index):
    screen.blit(bg_tile, (0,0))
    arrow_buttons = paste_background(screen, items_index=1)
    paste_clothes(screen, tops_list[tops_index], bottoms_list[bottoms_index], 
                  shoes_list[shoes_index], items_index=0)
    return arrow_buttons


def change_clothes(clothes_list, clothes_index, arrow):
    if arrow ==1:
        clothes_index += 1
        if clothes_index > (len(clothes_list)-1):
            clothes_index = 0
    if arrow ==2:
        clothes_index -= 1
        if clothes_index < 0:
            clothes_index = (len(clothes_list)-1)
    return clothes_index


def cycle_through_images(name, tops_list, tops_index, bottoms_list, 
                         bottoms_index, shoes_list, shoes_index):
    if name == 'tops_arrow_r':
        tops_index = change_clothes(tops_list, tops_index, arrow=1)
    if name == 'tops_arrow_l':
        tops_index = change_clothes(tops_list, tops_index, arrow=2)
    if name == 'bottoms_arrow_r':
        bottoms_index = change_clothes(bottoms_list, bottoms_index, arrow=1)
    if name == 'bottoms_arrow_l':
        bottoms_index = change_clothes(bottoms_list, bottoms_index, arrow=2)
    if name == 'shoes_arrow_r':
        shoes_index = change_clothes(shoes_list, shoes_index, arrow=1)
    if name == 'shoes_arrow_l':
        shoes_index = change_clothes(shoes_list, shoes_index, arrow=2)

    pygame.time.wait(300)
    return tops_index, bottoms_index, shoes_index


def run_program(screen, bg_tile, tops_list, tops_index, bottoms_list,
                bottoms_index, shoes_list, shoes_index):
    running = True
    while running: 
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                running = False
        
        buttons = load_screen(screen, bg_tile, tops_list, tops_index, 
                                    bottoms_list, bottoms_index, shoes_list, shoes_index)
        

        pos = pygame.mouse.get_pos()
        for name, rect in buttons.items():
            if rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]:
                    tops_index, bottoms_index, shoes_index = cycle_through_images(name, tops_list, tops_index, 
                                                                                  bottoms_list, bottoms_index, 
                                                                                  shoes_list, shoes_index)
                paste_clothes(screen, tops_list[tops_index], bottoms_list[bottoms_index], 
                              shoes_list[shoes_index], items_index=0)


        pygame.display.flip()
    pygame.quit()


def main():
    pygame.display.set_caption("Cher's Outfit Generator")
    resolution = (1920, 1080)
    screen = pygame.display.set_mode(resolution)
    bg_tile = (pygame.image.load("background/background.png").convert())
    tops_list = []
    tops_index = 0
    bottoms_list = []
    bottoms_index = 0
    shoes_list = []
    shoes_index = 0
    clothes_height = 280
    shoes_height = 140
    organize_items('tops', tops_list, clothes_height)
    organize_items('bottoms', bottoms_list, clothes_height)
    organize_items('shoes', shoes_list, shoes_height)
    run_program(screen, bg_tile, tops_list, tops_index, bottoms_list,
                bottoms_index, shoes_list, shoes_index)
		

if __name__ == "__main__":
	main()
