import pygame
import os
import ressources.color as color
import ressources.constants as constants
from toolbar import Toolbar

def valid_path(img_path: str) -> bool:
    return os.path.isfile(img_path)

# start pygame
pygame.init()
pygame.display.set_caption('draw your course')

img_path="ressources/malsaucy.png"
while not valid_path(img_path):
    img_path = input("Enter your image path :\n")

img = pygame.image.load(img_path)
HEIGHT = img.get_height()
if HEIGHT > constants.MAX_HEIGHT:
    img = pygame.transform.scale_by(img, constants.MAX_HEIGHT/HEIGHT)
    HEIGHT = img.get_height()
WIDTH = img.get_width()

screen = pygame.display.set_mode((WIDTH, HEIGHT + constants.ICONS_SIZE))
screen.blit(img, (0, 0))

# paint screen one time
pygame.display.flip()
running = True

toolbar = Toolbar(HEIGHT)

while (running):
    toolbar.draw(screen)
    # get events
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
            break;
            
        if i.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if i.button == 1:
                print(f"left click down at {pos}")
            if i.button == 3:
                print(f"right click down at {pos}")
            if pos[1] > HEIGHT:
                toolbar.click(pos)
                
        if i.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if i.button == 1:
                print(f"left click up at {pos}")
            if i.button == 3:
                print(f"right click up at {pos}")
 
# deactivates the pygame library
pygame.quit()