import pygame
from tkinter import filedialog as fd
import ressources.color as color
import ressources.constants as constants
from toolbar import Toolbar
from geometry.line import Line
from geometry.arc import Arc
from geometry.coord import Coord

img_path=fd.askopenfilename(title="Select your image")

# start pygame
pygame.init()
pygame.display.set_caption('Draw your course')

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

def draw_datas(surf, datas) :
    """Draw all the current forms

    Args:
        surf (pygame.Surface): The surface to draw the datas
        datas (list): the datas
    """
    for data in datas:
        data.draw(surf)
    pygame.display.flip()
    
def closest_point(datas, mouse) :
    """Get the closest coordinate of the mouse

    Args:
        datas (list): All forms
        mouse (Coord): Mouse coordinates

    Returns:
        Coord: Closest Coord if exists, else None
    """
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
                    
            if i.key == pygame.K_ESCAPE:
                preview = None
                tmp_points =[]
                print("Cancel form")
                
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


### Exemples
### Creation of false datas : dummy_data = [Line, Arc]
dummy_datas = []
dummy_coord = Coord(3, 5)
dummy_line = Line(Coord(0, 0), Coord(20, 32))
dummy_arc = Arc(Coord(32, 32), Coord(18, 20), Coord(65, 34))
dummy_datas.append(dummy_line)
dummy_datas.append(dummy_arc)


### Coord function
print("Coord methods :")
print(type(dummy_coord))
print(f"Coord.get_coord() : {dummy_coord.get_coord()}")
print(f"Coord.get_x() : {dummy_coord.get_x()}")
print(f"Coord.get_y() : {dummy_coord.get_y()}")
print(f"Coord(x, y) to create new Coord")
dummy_coord_2 = Coord(5, 10)
print(f"Coord.dist(Coord) for the Euclidian distance between 2 coord : {dummy_coord.dist(dummy_coord_2)}")

print("\n")
### Line function
### Reminder : dummy_data[0] is a Line object
### All point of each form use a Coord object. When you use Line.get_begin(), it will return a Coord object. Then, use get_coord() or get_x() to get the numeric datas
### exemple : dummy_line.get_begin() return a Coord object. dummy_line.get_begin().get_coord() return [0, 0]
print("Line methods :")
print(type(dummy_datas[0]))
print(f"Line.get_begin() (first point placed for the line): {dummy_line.get_begin().get_coord()}")
print(f"Line.get_end() (second point placed for the line): {dummy_line.get_end().get_coord()}")
print(f"Line.len() (len of the line): {dummy_line.len()}")
print(f"Line(Coord, Coord) to create a new Line")

print("\n")
### Arc functions
### Reminder : dummy_data[1] is a Arc object
### All point of each form use a Coord object. When you use Arc.get_C1(), it will return a Coord object. Then, use get_coord() or get_x() to get the numeric datas
### exemple : dummy_arc.get_C1() return a Coord object. dummy_arc.get_C1().get_coord() return [32, 32]
print("Arc methods :")
print(type(dummy_datas[1]))
print(f"Arc.get_C1() (first point placed for the Arc) : {dummy_arc.get_C1().get_coord()}")
print(f"Arc.get_C2() (second point placed for the Arc) : {dummy_arc.get_C2().get_coord()}")
print(f"Arc.get_C3() (third point placed for the Arc) : {dummy_arc.get_C1().get_coord()}")
print(f"Arc.get_center() (calculated center of the Arc) : {dummy_arc.get_center().get_coord()}")
print(f"Arc.get_angle() (angle of the arc in radians) : {dummy_arc.get_angle()}")
print(f"Arc.get_radius() (radius of the arc) : {dummy_arc.get_radius()}")
print(f"Arc.len() (len of the arc) : {dummy_arc.len()}")
