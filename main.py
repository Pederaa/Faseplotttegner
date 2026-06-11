from plotter import plotter
from diffEquations import diffEquations
from sympy import symbols, sin

from sympy import sin #Import all 
x, y, z = symbols('x y z')

sys1 = diffEquations(
    dx = (y-x)*(y+x),
    dy = x*(x+1)
)

sys2 = diffEquations(
    dx = sin(x),
    dy = y-1
)

if __name__ == "__main__":
    pl = plotter()
    pl.draw(sys2, [x, y])
