import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
import math

from sympy import lambdify

class plotter:
    def __init__(self) -> None:
        pass

    def getRanges(self, zeroes):
        x_range = [-3, 3]
        y_range = [-3, 3]

        return x_range, y_range

    def getZeros(self, system):
        return None
    
    def draw(self, equations, symbols, type="arrows"):
        Ndim = equations.len()
        if Ndim != len(symbols):
            raise ValueError(f"Number of equations does not match symbols: {Ndim} != {len(symbols)}")
        
        if Ndim == 1:
            pass

        elif Ndim == 2:
            self.draw2D(equations, symbols, type=type)
        
        elif Ndim == 3:
            print("Three dimensions is work in progress")
        
        else:
            raise ValueError(f"Cannot visualize {Ndim} dimensions")
        

    def draw2D(self, equations, symbols, type="arrows"):
        zeroes = self.getZeros(equations)
        x_range, y_range = self.getRanges(zeroes)

        n = 40
        xGrid, yGrid = np.meshgrid(np.linspace(x_range[0], x_range[1], n), 
                            np.linspace(y_range[0], y_range[1], n)
                    )

        f = lambdify((symbols[0], symbols[1]), equations.dx, 'numpy')
        g = lambdify((symbols[0], symbols[1]), equations.dy, 'numpy')
        dx = f(xGrid, yGrid)
        dy = g(xGrid, yGrid)

        magnitude = np.sqrt(dx**2 + dy**2)
        dx, dy = dx/magnitude, dy/magnitude

        # Draw the graph
        fig, ax = plt.subplots()

        match type:
            case "arrows":
                q = ax.quiver(xGrid, yGrid, dx, dy, magnitude, pivot='mid', scale_units='xy', scale=2*20/(x_range[1]-x_range[0]), cmap='inferno')
                plt.colorbar(q)

            case "lines":
                # Solve and plot trajectories from various starting points
                #initial_conditions = [(1/np.pi, 0), (1/(2*np.pi), 0), (1/(3*np.pi), 0), (1/(4*np.pi), 0)]
                #t_span = [0, 20]
                #t_eval = np.linspace(*t_span, 1000)

                #for x0, y0 in initial_conditions:
                #    sol = solve_ivp(system, t_span, [x0, y0], t_eval=t_eval)
                #    ax.plot(sol.y[0], sol.y[1])
                pass
        
        # Plots everytning in a plot
        ax.set_xlim(x_range)
        ax.set_ylim(y_range)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Phase portrait')

        plt.grid(True)
        #ax.legend()
        plt.show()