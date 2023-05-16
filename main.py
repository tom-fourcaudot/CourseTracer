import pygame
import color

# define constants
ICONS_SIZE = 100
MAX_HEIGHT = 700

# start pygame
pygame.init()

# get image dimension
img = pygame.image.load("Ressources/malsaucy.png")
pygame.display.set_caption('draw your course')

HEIGHT = img.get_height()
if HEIGHT > MAX_HEIGHT:
    img = pygame.transform.scale_by(img, MAX_HEIGHT/HEIGHT)
    HEIGHT = img.get_height()
    
WIDTH = img.get_width()

screen = pygame.display.set_mode((WIDTH, HEIGHT + ICONS_SIZE))
screen.blit(img, (0, 0))

# paint screen one time
pygame.display.flip()
running = True


while (running):
    # get events
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False
            
        if i.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if i.button == 1:
                print(f"left click down at {pos}")
            if i.button == 3:
                print(f"right click down at {pos}")
            if pos[1] > HEIGHT:
                print(f"in toolbar, icon number {int(pos[0]/ICONS_SIZE)}")
                
        if i.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if i.button == 1:
                print(f"left click up at {pos}")
            if i.button == 3:
                print(f"right click up at {pos}")
 
# deactivates the pygame library
pygame.quit()