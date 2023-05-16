import pygame
import ressources.color as color
import ressources.constants as constants
from geometry.coord import Coord

class Icon:
    name: str
    img: str
    number: int
    coord: Coord
    active: bool
    
    def __init__(self, name: str, img: str, number: int, toolbar_height: int) -> None:
        self.name = name
        self.img = pygame.image.load(f"ressources/icons/{img}.png").convert_alpha()
        self.number = number
        self.active = False
        self.coord = Coord(self.number*constants.ICONS_SIZE, toolbar_height)
        
    def draw(self, bg_color: pygame.Color, surf: pygame.Surface) -> None:
        pygame.draw.rect(surf, bg_color, pygame.Rect(self.coord.get_x(), self.coord.get_y(), constants.ICONS_SIZE, constants.ICONS_SIZE))
        surf.blit(self.img, (self.coord.get_x(), self.coord.get_y()))
        
class Toolbar:    
    icons: list
    actives: list
    
    def __init__(self, height: int) -> None:
        self.icons = []
        self.icons.append(Icon("Move", "move", 0, height))
        self.icons.append(Icon("Delete", "delete", 1, height))
        self.icons.append(Icon("Draw line", "line", 2, height))
        self.icons.append(Icon("Draw arc", "arc", 3, height))
        self.actives = [False for i in range(len(self.icons))]
        
    def draw(self, surf: pygame.Surface):
        for icon, active in zip(self.icons, self.actives):
            if active:
                icon_color = color.cyan
            else:
                icon_color = color.white
            icon.draw(icon_color, surf)
        pygame.display.flip()
        
    def click(self, coord):
        icon_number = int(coord[0]/constants.ICONS_SIZE)
        if icon_number < len(self.icons):
            self.actives = [False for i in range(len(self.icons))]
            self.actives[icon_number] = True
            
    def get_actives(self):
        return self.actives