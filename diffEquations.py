class diffEquations:
    def __init__(self, dx=None, dy=None, dz=None) -> None:
        self.dx = dx
        self.dy = dy
        self.dz = dz

        if self.dy == None:
            self.rank = 1
        elif self.dz == None:
            self.rank = 2
        else:
            self.rank = 3
        
    def len(self):
        return self.rank
    
    def getList(self):
        l = [self.dx, self.dy, self.dz]
        return l[0:self.rank]