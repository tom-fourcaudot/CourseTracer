import pygame
import ressources.color as color
import ressources.constants as constants
from geometry.coord import Coord

class Icon:
    """name: str
    img: str
    number: int
    coord: Coord
    active: bool"""
    
    def __init__(self, name, img, number, toolbar_height) :
        """Constructor of a Icon

        Args:
            name (str): Name of the Icon
            img (str): Image path of the Icon
            number (int): The n th Icon in the toolbar
            toolbar_height (int): The height to draw the icons
        """
        self.name = name
        self.img = pygame.image.load(f"ressources/icons/{img}.png").convert_alpha()
        self.number = number
        self.active = False
        self.coord = Coord(self.number*constants.ICONS_SIZE, toolbar_height)
        
    def draw(self, bg_color, surf) :
        """draw the icons on a surface

        Args:
            bg_color (pygame.Color): background color of the icon
            surf (pygame.Surface): the surface to draw
        """
        pygame.draw.rect(surf, bg_color, pygame.Rect(self.coord.get_x(), self.coord.get_y(), constants.ICONS_SIZE, constants.ICONS_SIZE))
        surf.blit(self.img, (self.coord.get_x(), self.coord.get_y()))
        
class Toolbar:    
    """icons: list[Icon]
    actives: int"""
    
    def __init__(self, height) :
        """Constructor of the Toolbar

        Args:
            height (int): Toolbar height
        """
        self.icons = []
        self.icons.append(Icon("Move", "move", 0, height))
        self.icons.append(Icon("Delete", "delete", 1, height))
        self.icons.append(Icon("Draw line", "line", 2, height))
        self.icons.append(Icon("Draw arc", "arc", 3, height))
        self.active = 0
        
    def draw(self, surf):
        """Draw the toolbar on a surface

        Args:
            surf (pygame.Surface): the surface to draw
        """
        for icon in self.icons:
            if icon.number == self.active:
                icon_color = color.cyan
            else:
                icon_color = color.white
            icon.draw(icon_color, surf)
        pygame.display.flip()
        
    def click(self, coord):
        """Handle the click on the toolbar

        Args:
            coord (Coord): Coordinate of the click
        """
        icon_number = int(coord.get_x()/constants.ICONS_SIZE)
        if icon_number < len(self.icons):
            self.active = icon_number
            
    def get_actives(self):
        """Return the number of the active icon

        Returns:
            int: the number of the active icon
        """
        return self.active