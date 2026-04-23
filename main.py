from plotter import plotter
from diffEquations import diffEquations
from sympy import symbols


x, y, z = symbols('x y z')

sys = diffEquations(
    dx = (y-x)*(y+x),
    dy = x*(x+1)
)

if __name__ == "__main__":
    pl = plotter()
    pl.draw(sys, [x, y])