from coord import Coord

class Arc:
    begin: Coord
    end: Coord
    center: Coord
    
    def __init__(self) -> None:
        self.begin = None
        self.end = None
        self.center = None
        
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