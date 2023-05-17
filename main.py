import pygame
import os
import ressources.color as color
import ressources.constants as constants
from toolbar import Toolbar
from geometry.line import Line
from geometry.arc import Arc
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
clock = pygame.time.Clock()
toolbar = Toolbar(HEIGHT)

########################################################################################
datas = []
tmp_points = []
mode = None
preview = None
arc_way = False
ctrl_pressed = False
closer = None

def draw_datas(surf: pygame.Surface, datas: list) -> None:
    for data in datas:
        data.draw(surf)
    pygame.display.flip()
    
def closest_point(datas: list, mouse: Coord) -> Coord:
    min_d = 99999
    best  = None
    for elem in datas:
        tmp = elem.close(mouse, min_d)
        if tmp[1] != None:
            best = tmp[1]
            min_d = tmp[0]
    return best

while (running):
    clock.tick(30)
    mouse_coord = Coord(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    screen.blit(img, (0, 0))
    toolbar.draw(screen)
    draw_datas(screen, datas)
    mode = toolbar.get_actives()
    # get events
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
            break;
        
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LCTRL:
                ctrl_pressed = True
                closer = closest_point(datas, mouse_coord)
                
            if i.key == pygame.K_BACKSPACE:
                if len(datas) > 0:
                    datas.pop(-1)
                    print("Remove last draw element")
                    
            if i.key == pygame.K_SPACE:
                datas = []
                print("Reset the drawing")
        
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_LCTRL:
                ctrl_pressed = False
            
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: # left click
                if mouse_coord.get_y() > HEIGHT:
                    old_mode = mode
                    toolbar.click(mouse_coord)
                    mode = toolbar.get_actives()
                    if old_mode != mode:
                        tmp_points = []
                        preview = None
                else:
                    if mode == 2: #line mode
                        if ctrl_pressed and closer != None:
                            tmp_points.append(closer)
                        else:
                            tmp_points.append(mouse_coord)                     
                        if len(tmp_points) == 2:
                            preview = None
                            datas.append(Line(tmp_points[0], tmp_points[1]))
                            tmp_points = []
                            print("New line")
                    
                    if mode == 3: # arc mode
                        if ctrl_pressed and closer != None:
                            tmp_points.append(closer)
                        else:
                            tmp_points.append(mouse_coord)
                        if len(tmp_points) == 3:
                            preview = None
                            datas.append(Arc(tmp_points[0], tmp_points[1], tmp_points[2], arc_way))
                            tmp_points = []
                            print("New arc")
                        
            if i.button == 3: # right click
                if mode == 3:
                    arc_way = not arc_way

        if i.type == pygame.MOUSEMOTION:
            if mode == 2:
                if len(tmp_points) == 1:
                    preview = Line(tmp_points[0], mouse_coord)
            
            if mode == 3:
                if len(tmp_points) == 1:
                    preview = Line(tmp_points[0], mouse_coord)
                if len(tmp_points) == 2:
                    preview = Arc(tmp_points[0], tmp_points[1], mouse_coord, arc_way)
       
    # draw preview         
    if preview != None:
        preview.draw(screen, color.blue)
        
    if ctrl_pressed:
        closest = closest_point(datas, mouse_coord)
        if closest != None:
            pygame.draw.circle(screen, color.green, closest.get_coord(), 5, 5)
    pygame.display.flip()
# deactivates the pygame library
pygame.quit()