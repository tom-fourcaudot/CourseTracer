import pygame
import os
import ressources.color as color
import ressources.constants as constants
from toolbar import Toolbar
from geometry.line import Line
from geometry.coord import Coord

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
# paint screen one time
pygame.display.flip()
running = True
toolbar = Toolbar(HEIGHT)

########################################################################################
datas = []
tmp_points = []
mode = None
preview = None

def draw_datas(surf: pygame.Surface, datas: list) -> None:
    for data in datas:
        data.draw(surf)
    pygame.display.flip()

while (running):
    screen.blit(img, (0, 0))
    toolbar.draw(screen)
    draw_datas(screen, datas)
    mode = toolbar.get_actives()
    # get events
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
            break;
            
        if i.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if i.button == 1:
                if pos[1] > HEIGHT:
                    old_mode = mode
                    toolbar.click(pos)
                    mode = toolbar.get_actives()
                    if old_mode != mode:
                        tmp_points = []
                        preview = None
                else:
                    if mode == 2: #line mode
                        tmp_points.append(Coord(pos[0], pos[1]))
                        if len(tmp_points) == 2:
                            preview = None
                            datas.append(Line(tmp_points[0], tmp_points[1]))
                            tmp_points = []
                            print("New line")

        if i.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            if mode == 2:
                if len(tmp_points) == 1:
                    preview = Line(tmp_points[0], Coord(mouse_pos[0], mouse_pos[1]))
    if preview != None:
        preview.draw(screen, color.blue)
    pygame.display.flip()
# deactivates the pygame library
pygame.quit()