from plotter import plotter
from diffEquations import diffEquations
from sympy import symbols, sin

from sympy import sin #Import all 
x, y, z = symbols('x y z')

sys1 = diffEquations(
    dx = (y-x)*(y+x),
    dy = x*(x+1)
)

rabbit_fox = diffEquations(
    dx = x*(63 - 5*y),
    dy = -y*(457 - 6*x)
)

a = 4
b = 1
c = 1
sys2 = diffEquations(
    dx = -a*x - y**2,
    dy = b*x*y + c*y
)


if __name__ == "__main__":
    pl = plotter()
    # pl.draw(sys2, [x, y], x_range=[-0.75, -1.25], y_range=[1.75, 2.75])
    pl.draw(sys2, [x, y], x_range=[-5, 5], y_range=[-5, 5])
