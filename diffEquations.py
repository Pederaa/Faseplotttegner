class diffEquations:
    def __init__(self, dx=None, dy=None, dz=None) -> None:
        self.dx = dx
        self.dy = dy
        self.dz = dz
    
    def len(self):
        if self.dy == None:
            return 1
        elif self.dz == None:
            return 2
        else:
            return 3