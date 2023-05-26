import pygame
import ressources.color as color
from geometry.coord import Coord

class Line:
    """Class Line
    use to represent and edit a line with 2 Coordinates
    """
    """begin: Coord # first point of the Line
    end: Coord # last point of the line"""
    
    def __init__(self, begin = None, end = None) :
        """Simple constructor of the Line.
        Set all datas to None. Please use the setters
        """
        self.begin = begin
        self.end = end
    
    def get_begin(self) :
        """Getter of begin

        Returns:
            Coord: the Coord object, describing the begin of the line
        """
        return self.begin
    
    def set_begin(self, new_C) :
        """Setter of begin coordinates

        Args:
            new_C (Coord): the new Coord object
        """
        self.begin = new_C
        
    def set_begin(self, x, y) :
        """Setter of begin coordinates

        Args:
            x (float): x element of the begin coordinates
            y (float): y element of the begin coordinates
        """
        tmp_C = Coord(x, y)
        self.begin = tmp_C
        
    def get_end(self) :
        """Getter of end

        Returns:
            Coord: the Coord object, describing the end of the line
        """
        return self.end
    
    def set_end(self, new_C) :
        """Setter of end coordinates

        Args:
            new_C (Coord): the new Coord object
        """
        self.end = new_C
        
    def set_end(self, x, y) :
        """Setter of end coordinates

        Args:
            x (float): x element of the end coordinates
            y (float): y element of the end coordinates
        """
        tmp_C = Coord(x, y)
        self.end = tmp_C
        
    def draw(self, surf, col = color.red):
        """draw the form on the surface

        Args:
            surf (pygame.Surface): The surface we want to draw
            col (ressources.Color, optional): the color oh the form. Defaults to color.red.
        """
        pygame.draw.line(surf, col, self.begin.get_coord(), self.end.get_coord(), width=3)
        
    def close(self, mouse, min_d):
        """Find the closet point between mouse and return the coordinates, only if the distance is below min_d

        Args:
            mouse (Coord): the mouse Coordinate
            min_d (float): the min distance

        Returns:
            Tupple(float, Coord): the new min distance and the associate coordinates.
        """
        tmp = None
        
        begin_dist = mouse.dist(self.begin)
        if min(min_d, begin_dist) != min_d:
            min_d = begin_dist
            tmp = self.begin
            
        end_dist =  mouse.dist(self.end)
        if min(min_d, end_dist) != min_d:
            min_d = end_dist
            tmp = self.end
        
        return (min_d, tmp)
    
    def len(self) -> float:
        """Return the len of the Line

        Returns:
            float: len of the Line
        """
        return self.begin.dist(self.end)