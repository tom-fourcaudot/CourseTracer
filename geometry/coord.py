import math

class Coord:
    """Class Coord
    use to represent Coordinate in a 2d space
    """
    
    x: float # x element of a coordinate
    y: float # y element of a coordinate
    
    def __init__(self, x: float, y: float) -> None:
        """Constructor of a Coord object

        Args:
            x (float): x element of the Coord object
            y (float): y element of the Coord object
        """
        self.x = x
        self.y = y
        
    def get_x(self) -> float:
        """Getter of x

        Returns:
            float: the x element of the Coord object
        """
        return self.x
    
    def set_x(self, new_x: float) -> None:
        """Setter of x

        Args:
            new_x (float): the new x element of the Coord object
        """
        self.x = new_x
    
    def get_y(self) -> None:
        """Getter of y

        Returns:
            float: the y element of the Coord object
        """
        return self.y
    
    def set_y(self, new_y: float) -> None:
        """Setter of y

        Args:
            new_y (float): the new y element of the Coord object
        """
        self.y = new_y
    
    def get_coord(self) -> float:
        """Getter of the object, as a tupple

        Returns:
            (float, float): the tupple (x, y) of the coord object
        """
        return (self.x, self.y)
    
    def dist(self, c) -> float:
        return math.dist(self.get_coord(), c.get_coord())