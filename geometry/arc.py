import math
import numpy as np
import pygame
import ressources.color as color
from geometry.coord import Coord

class Arc:
    """
    C1: Coord # begin of the arc
    C2: Coord # intermediate point of the arc
    C3: Coord # end of the arc
    center: Coord # center of the arc
    radius: float # radius of the arc
    start_angle: float #start angle of the arc, for pygame
    end_angle: float # end angle of the arc, for pygame
    """
    
    def __init__(self, C1, C2, C3, way = False):
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
        self.calculate_thetas(way)
        if way:
            tmp = self.start_angle
            self.start_angle = self.end_angle
            self.end_angle = tmp
        
    def get_C1(self):
        """Getter of begin

        Returns:
            Coord: the Coord object, describing the first point of the arc
        """
        return self.C1
    
    def set_C1(self, new_C) :
        """Setter of C1 coordinates

        Args:
            new_C (Coord): the new Coord object
        """
        self.C1 = new_C
        
    def set_C1(self, x, y) :
        """Setter of C1 coordinates

        Args:
            x (float): x element of the C1 coordinates
            y (float): y element of the C1 coordinates
        """
        tmp_C = Coord(x, y)
        self.C1 = tmp_C
        
    def get_C2(self) :
        """Getter of C2 coordinate

        Returns:
            Coord: the Coord object, describing the second point of the arc
        """
        return self.C2
    
    def set_C2(self, new_C) :
        """Setter of C2 coordinates

        Args:
            new_C (Coord): the new Coord object
        """
        self.C2 = new_C
        
    def set_C2(self, x, y) :
        """Setter of C2 coordinates

        Args:
            x (float): x element of the C2 coordinates
            y (float): y element of the C2 coordinates
        """
        tmp_C = Coord(x, y)
        self.C2 = tmp_C
        
    def get_C3(self) :
        """Getter of C3 coordinate

        Returns:
            Coord: the Coord object, describing the last point of the arc
        """
        return self.C3
    
    def set_C3(self, new_C):
        """Setter of C3 coordinates

        Args:
            new_C (Coord): the new Coord object
        """
        self.C3 = new_C
        
    def set_C3(self, x, y):
        """Setter of C3 coordinates

        Args:
            x (float): x element of the C3 coordinates
            y (float): y element of the C3 coordinates
        """
        tmp_C = Coord(x, y)
        self.C3 = tmp_C
        
    def get_center(self) :
        """Getter of center

        Returns:
            Coord: the Coord object, describing the center of the line
        """
        return self.begin
    
    def set_center(self, new_C) :
        """Setter of center coordinates

        Args:
            new_C (Coord): the new Coord object
        """
        self.center = new_C
        
    def set_center(self, x, y) :
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
        
    def calculate_thetas(self, way):
        try:
            relative_begin_coord = Coord(self.C1.get_x() - self.center.get_x(), self.C1.get_y() - self.center.get_y())
            relative_end_coord_1 = Coord(self.C2.get_x() - self.center.get_x(), self.C2.get_y() - self.center.get_y())
            relative_end_coord_2 = Coord(self.C3.get_x() - self.center.get_x(), self.C3.get_y() - self.center.get_y())
            self.start_angle = math.atan2(-relative_begin_coord.get_y(), relative_begin_coord.get_x())
            end_angle_1 = math.atan2(-relative_end_coord_1.get_y(), relative_end_coord_1.get_x())
            end_angle_2 = math.atan2(-relative_end_coord_2.get_y(), relative_end_coord_2.get_x())
            tmp1 = end_angle_1 - self.start_angle + math.pi + math.pi if end_angle_1 - self.start_angle < 0 else end_angle_1
            tmp2 = end_angle_2 - self.start_angle + math.pi + math.pi if end_angle_2 - self.start_angle < 0 else end_angle_2
            if tmp1 > tmp2 :
                self.end_angle = end_angle_2 if way else end_angle_1
            else:
                self.end_angle = end_angle_1 if way else end_angle_2
        except :
            self.start_angle = 0
            self.end_angle = 0
            
    def draw(self, surf, col = color.red):
        if self.center != None:
            bound_origin = Coord(self.center.get_x() - self.radius, self.center.get_y() - self.radius)
            bound = pygame.Rect(bound_origin.get_x(), bound_origin.get_y(), self.radius*2, self.radius*2)
            pygame.draw.circle(surf, color.violet, self.center.get_coord(), 2, 2)
            pygame.draw.arc(surf, col, bound, self.start_angle, self.end_angle, 3)
        else:
            pygame.draw.line(surf, col, self.C1.get_coord(), self.C2.get_coord(), 3)
        pygame.draw.circle(surf, color.red, self.C1.get_coord(), 2, 2)
        pygame.draw.circle(surf, color.red, self.C2.get_coord(), 2, 2)
        
    def close(self, mouse, min_d):
        tmp = None
        
        c1_dist = mouse.dist(self.C1)
        if min(min_d, c1_dist) != min_d:
            min_d = c1_dist
            tmp = self.C1
            
        c2_dist = mouse.dist(self.C2)
        if min(min_d, c2_dist) != min_d:
            min_d = c2_dist
            tmp = self.C2
            
        c3_dist = mouse.dist(self.C3)
        if min(min_d, c3_dist) != min_d:
            min_d = c3_dist
            tmp = self.C3
        
        return (min_d, tmp)