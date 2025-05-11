# Cher's Outfit Generator

## Demo
Demo Video: <URL>

## GitHub Repository
GitHub Repo: <https://github.com/camillebrisman/final-project.git>

## Description
Cher's Outfit Generator is a program that allows the user to create, save, and 
orgainize outfits by cycling through images of their tops, bottoms, and shoes, 
similarly to the iconic outfit generator from the movie *Clueless*. 

## Features
- Browse and display clothing items by category
- Cycle through clothing items with arrow buttons
- Randomize clothing items or entire outfit combinations
- Save outfits into seasonal folders
- Name saved outifts
- Auto-resizes and renames uploaded images of clothing items for organization

## Set Up
1. Install 3rd party libraries listed in the requirements.txt
2. Upload images of clothing items into their corresponding folders (upload
   tops into the "tops" folder, etc.)
- NOTE: 
    1. Example images of clothing are provided in the "tops", "bottoms", and 
       "shoes" folders-- these can be removed and replaced for a personalized 
       experience.
    2. If uploading images, ensure that the file types are identifiable--
       for example, some identifiable file types include .png or .jpg, and some
       non-identifiable file types include .avif files.

## Folder Structure
1. Folders should follow this layout:

```
    src/
    │
    ├── background/
    │   ├── background.png
    │   ├── title_icon.png
    │   ├── save_group.png
    │   ├── right_arrow.png
    │   ├── left_arrow.png
    │   └── randomize_group.png
    │
    ├── tops/
    ├── bottoms/
    ├── shoes/
    │
    └── seasons/
        ├── spring/
        ├── summer/
        ├── fall/
        └── winter/
```

2. Uploaded images of clothing are stored in their respective folders (tops in 
   the "tops" folder, etc.).
3. Saved outfits are stored in the "seasons" subfolder that was chosen when the
   outfit was saved.

## Running The Program
- When the program is run, all images in the "tops", "bottoms", and "shoes" 
  folders will be automatically renamed and resized for organization and 
  display purposes.
- The user can cycle forwards and backwards through each clothing catagory 
  using the left and right arrows on the sides of the images.
- To randomize items in a catagory, the user can click on the title of the
  catagory they would like to randomize in the "Randomize" section located to
  the right of the displayed clothing items. The user can also click on the 
  "Outfit" title in the "Randomize" section to randomize all catagories 
  simultaneously.
- To save an outfit, the user can click on the folder of the season they would
  like to catogorize the outfit in. These folders are located in the "Save" 
  section on the left of the displayed clothing items. Once the desired folder
  is selected, a text box will appear in the center of the "Save" section, 
  prompting the user to type the name they would like to save their outfit as.
  Once the user presses "Enter" on their keyboard, a cropped image of the 
  display showing only the clothing items and background will be saved with the 
  inputed name in the selected folder. If no name is input, the outfit will be 
  saved with name of the season chosen and a numerical increment suffix.
- To exit the program, press "Escape" on the keyboard, or click the "X" at the
  top of the display window.

## Additional Notes
- Program should be run in full HD resolution (1920 x 1080)
- Do not remove or modify images* in the "background" folder -- this folder
  contains the graphics used to create buttons and the background display.
- When the program is run, images in the "tops", "bottoms", and "shoes" folders
  will be saved as .jpgs so that the item of clothing has a border and is not 
  displayed directly onto the background.

*if desired the "background.png" image in the "background" folder may be 
replaced by a 1920 x 1080 .png image titled "background.png".

## Resources
- https://www.youtube.com/shorts/ww57H0n9has
- https://www.youtube.com/watch?v=Rvcyf4HsWiw
- https://www.youtube.com/watch?v=G8MYGDf_9ho
