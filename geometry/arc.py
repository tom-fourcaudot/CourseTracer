import math
import numpy as np
import pygame
import ressources.color as color
from geometry.coord import Coord

class Arc:
    C1: Coord # begin of the arc
    C2: Coord # intermediate point of the arc
    C3: Coord # end of the arc
    center: Coord # center of the arc
    radius: float # radius of the arc
    start_angle: float #start angle of the arc, for pygame
    end_angle: float # end angle of the arc, for pygame
    
    def __init__(self, C1: Coord, C2: Coord, C3: Coord, way : bool = False) -> None:
        """Constructor of the Arc
        Set all values to None. Please use the setter.
        """
        self.C1 = C1
        self.C2 = C2
        self.C3 = C3
        self.center = None
        self.radius = None
        self.start_angle = None
        self.end_angle = None
        self.calculate_center()
        self.calculate_thetas()
        if way:
            tmp = self.start_angle
            self.start_angle = self.end_angle
            self.end_angle = tmp
        
    def get_C1(self) -> Coord:
        """Getter of begin

        Returns:
            Coord: the Coord object, describing the first point of the arc
        """
        return self.C1
    
    def set_C1(self, new_C: Coord) -> None:
        """Setter of C1 coordinates

        Args:
            new_C (Coord): the new Coord object
        """
        self.C1 = new_C
        
    def set_C1(self, x: float, y: float) -> None:
        """Setter of C1 coordinates

        Args:
            x (float): x element of the C1 coordinates
            y (float): y element of the C1 coordinates
        """
        tmp_C = Coord(x, y)
        self.C1 = tmp_C
        
    def get_C2(self) -> Coord:
        """Getter of C2 coordinate

        Returns:
            Coord: the Coord object, describing the second point of the arc
        """
        return self.C2
    
    def set_C2(self, new_C: Coord) -> None:
        """Setter of C2 coordinates

        Args:
            new_C (Coord): the new Coord object
        """
        self.C2 = new_C
        
    def set_C2(self, x: float, y: float) -> None:
        """Setter of C2 coordinates

        Args:
            x (float): x element of the C2 coordinates
            y (float): y element of the C2 coordinates
        """
        tmp_C = Coord(x, y)
        self.C2 = tmp_C
        
    def get_C3(self) -> Coord:
        """Getter of C3 coordinate

        Returns:
            Coord: the Coord object, describing the last point of the arc
        """
        return self.C3
    
    def set_C3(self, new_C: Coord) -> None:
        """Setter of C3 coordinates

        Args:
            new_C (Coord): the new Coord object
        """
        self.C3 = new_C
        
    def set_C3(self, x: float, y: float) -> None:
        """Setter of C3 coordinates

        Args:
            x (float): x element of the C3 coordinates
            y (float): y element of the C3 coordinates
        """
        tmp_C = Coord(x, y)
        self.C3 = tmp_C
        
    def get_center(self) -> Coord:
        """Getter of center

        Returns:
            Coord: the Coord object, describing the center of the line
        """
        return self.begin
    
    def set_center(self, new_C: Coord) -> None:
        """Setter of center coordinates

        Args:
            new_C (Coord): the new Coord object
        """
        self.center = new_C
        
    def set_center(self, x: float, y: float) -> None:
        """Setter of center coordinates

        Args:
            x (float): x element of the center coordinates
            y (float): y element of the center coordinates
        """
        tmp_C = Coord(x, y)
        self.center = tmp_C
        
    def calculate_center(self):
        """
        Returns the center and radius of the circle passing the given 3 points.
        In case the 3 points form a line, returns (None, infinity).
        """
        p1 = self.C1.get_coord()
        p2 = self.C2.get_coord()
        p3 = self.C3.get_coord()
        temp = p2[0] * p2[0] + p2[1] * p2[1]
        bc = (p1[0] * p1[0] + p1[1] * p1[1] - temp) / 2
        cd = (temp - p3[0] * p3[0] - p3[1] * p3[1]) / 2
        det = (p1[0] - p2[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p2[1])
        
        if abs(det) < 1.0e-6:
            return (None, np.inf)
        
        # Center of circle
        cx = (bc*(p2[1] - p3[1]) - cd*(p1[1] - p2[1])) / det
        cy = ((p1[0] - p2[0]) * cd - (p2[0] - p3[0]) * bc) / det
        
        self.radius = np.sqrt((cx - p1[0])**2 + (cy - p1[1])**2)
        self.set_center(cx, cy)
        
    def calculate_thetas(self):
        try:
            relative_begin_coord = Coord(self.C1.get_x() - self.center.get_x(), self.C1.get_y() - self.center.get_y())
            relative_end_coord = Coord(self.C2.get_x() - self.center.get_x(), self.C2.get_y() - self.center.get_y())
            self.start_angle = math.atan2(-relative_begin_coord.get_y(), relative_begin_coord.get_x())
            self.end_angle = math.atan2(-relative_end_coord.get_y(), relative_end_coord.get_x())
        except :
            self.start_angle = 0
            self.end_angle = 0
            
    
        
        
    def draw(self, surf: pygame.Surface, col: pygame.Color = color.red):
        bound_origin = Coord(self.center.get_x() - self.radius, self.center.get_y() - self.radius)
        bound = pygame.Rect(bound_origin.get_x(), bound_origin.get_y(), self.radius*2, self.radius*2)
        pygame.draw.arc(surf, col, bound, self.start_angle, self.end_angle, 3)
        pygame.draw.circle(surf, color.violet, self.center.get_coord(), 2, 2)
        pygame.draw.circle(surf, color.red, self.C1.get_coord(), 2, 2)
        pygame.draw.circle(surf, color.red, self.C2.get_coord(), 2, 2)