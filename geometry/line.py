import pygame
import ressources.color as color
from geometry.coord import Coord

class Line:
    """Class Line
    use to represent and edit a line with 2 Coordinates
    """
    begin: Coord # first point of the Line
    end: Coord # last point of the line
    
    def __init__(self, begin : Coord = None, end : Coord = None) -> None:
        """Simple constructor of the Line.
        Set all datas to None. Please use the setters
        """
        self.begin = begin
        self.end = end
    
    def get_begin(self) -> Coord:
        """Getter of begin

        Returns:
            Coord: the Coord object, describing the begin of the line
        """
        return self.begin
    
    def set_begin(self, new_C: Coord) -> None:
        """Setter of begin coordinates

        Args:
            new_C (Coord): the new Coord object
        """
        self.begin = new_C
        
    def set_begin(self, x: float, y: float) -> None:
        """Setter of begin coordinates

        Args:
            x (float): x element of the begin coordinates
            y (float): y element of the begin coordinates
        """
        tmp_C = Coord(x, y)
        self.begin = tmp_C
        
    def get_end(self) -> Coord:
        """Getter of end

        Returns:
            Coord: the Coord object, describing the end of the line
        """
        return self.end
    
    def set_end(self, new_C: Coord) -> None:
        """Setter of end coordinates

        Args:
            new_C (Coord): the new Coord object
        """
        self.end = new_C
        
    def set_end(self, x: float, y: float) -> None:
        """Setter of end coordinates

        Args:
            x (float): x element of the end coordinates
            y (float): y element of the end coordinates
        """
        tmp_C = Coord(x, y)
        self.end = tmp_C
        
    def draw(self, surf: pygame.Surface, col = color.red):
        pygame.draw.line(surf, col, self.begin.get_coord(), self.end.get_coord(), width=3)