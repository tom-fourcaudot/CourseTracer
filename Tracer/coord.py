class Coord:
    x: float
    y: float
    
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
        
    def get_x(self) -> float:
        return self.x
    
    def set_x(self, new_x: float) -> None:
        self.x = new_x
    
    def get_y(self) -> None:
        return self.y
    
    def set_y(self, new_y: float) -> None:
        self.y = new_y
    
    def get_coord(self) -> float:
        return (self.x, self.y)
    