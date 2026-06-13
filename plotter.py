import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
import math

from sympy import lambdify, FiniteSet, Interval, ProductSet, ImageSet, ComplexRegion, ConditionSet, Naturals, Naturals0, Integers, Reals, Complexes, EmptySet, ConditionSet
from sympy.solvers import solve, solveset, nonlinsolve
from sympy.core.containers import Tuple
from sympy.core.numbers import Number
import sympy

class plotter:
    def __init__(self) -> None:
        pass

    def getRanges(self, zeroes):
        if len(zeroes) == 0:
            x_range = [-10, 10]
            y_range = [-10, 10]
            return x_range, y_range
        
        elif len(zeroes) == 1:
            x_range = [-10, 10]
            y_range = [-10, 10]
            return x_range, y_range
        
        x_range = [0.0, 0.0]
        y_range = [0.0, 0.0]

        for zero in zeroes:
            x = zero[0]
            if x < x_range[0]:
                x_range[0] = x
            elif x > x_range[1]:
                x_range[1] = x
            
            y = zero[1]
            if y < y_range[0]:
                y_range[0] = y
            elif y > y_range[1]:
                y_range[1] = y
        
        x_width = abs(x_range[1] - x_range[0])
        y_width = abs(y_range[1] - y_range[0])

        if x_width > y_width:
            y_width = x_width
            y_range[0] -= (x_width - y_width)/2
            y_range[1] += (x_width - y_width)/2
        else:
            x_width = y_width
            x_range[0] -= (y_width - x_width)/2
            x_range[1] += (y_width - x_width)/2
        
        x_range[0] = float(x_range[0] - x_width*0.2)
        x_range[1] = float(x_range[1] + x_width*0.2)
        y_range[0] = float(y_range[0] - y_width*0.2)
        y_range[1] = float(y_range[1] + y_width*0.2)

        return x_range, y_range
       

    def getZeros(self, system, symbols):
        p = nonlinsolve(system.getList(), symbols)
        
        zeroes = []
        if isinstance(p, FiniteSet):
            for s in p:
                zeroes.extend(self.iterateZero(s))
        
        else:
            zeroes.extend(self.iterateZero(p))
        
        return zeroes
    
    def iterateZero(self, s):
        x = self.extractPointFromSet(s[0])
        y = self.extractPointFromSet(s[1])

        zeroes = []
        for i in x:
            for j in y:
                zeroes.append((i, j))
        return zeroes


    def extractPointFromSet(self, setToExtract):
        if isinstance(setToExtract, int) or isinstance(setToExtract, float) or isinstance(setToExtract, Number):
            return [setToExtract]
        
        if isinstance(setToExtract, ConditionSet):
            raise ValueError("Unhandled type of zeroes: ConditionSet", setToExtract)

        elif isinstance(setToExtract, FiniteSet):
            raise ValueError("Unhandled type of zeroes: FiniteSet", p)
        
        elif isinstance(setToExtract, Interval):
            raise ValueError("Unhandled type of zeroes: Interval", setToExtract)
        
        elif isinstance(setToExtract, ProductSet):
            raise ValueError("Unhandled type of zeroes: ProductSet", setToExtract)
        
        elif isinstance(setToExtract, ImageSet):
            values = []
            for i in range(-2, 3):
                values.append(setToExtract.lamda(i))
            return values
        
        elif isinstance(setToExtract, ComplexRegion):
            raise ValueError("Unhandled type of zeroes: ComplexRegion", setToExtract)
        
        # elif isinstance(s, Naturals):
        #     raise ValueError("Unhandled type of zeroes: Naturals", s)
        
        # elif isinstance(s, Naturals0):
        #     raise ValueError("Unhandled type of zeroes: Naturals0", s)
        
        # elif isinstance(s, Reals):
        #     raise ValueError("Unhandled type of zeroes: Reals", s)
        
        # elif isinstance(s, Complexes):
        #     raise ValueError("Unhandled type of zeroes: Complexes", s)
        
        # elif isinstance(s, EmptySet):
        #     pass 

        else:
            raise ValueError("Unidentified type of zeroes", setToExtract)        
    
    
    def draw(self, equations, symbols, linetype="arrows"):
        Ndim = equations.len()
        if Ndim != len(symbols):
            raise ValueError(f"Number of equations does not match symbols: {Ndim} != {len(symbols)}")
        
        if Ndim == 1:
             print("One dimensions is work in progress")

        elif Ndim == 2:
            self.draw2D(equations, symbols, linetype=linetype)
        
        elif Ndim == 3:
            print("Three dimensions is work in progress")
        
        else:
            raise ValueError(f"Cannot visualize {Ndim} dimensions")
        

    def draw2D(self, equations, symbols, linetype="arrows"):
        zeroes = self.getZeros(equations, symbols)
        x_range, y_range = self.getRanges(zeroes)

        n = 20
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

        x_zeroes = [float(p[0]) for p in zeroes]
        y_zeroes = [float(p[1]) for p in zeroes]
        plt.scatter(x_zeroes, y_zeroes, marker='o', c="Red", s=50)

        match linetype:
            case "arrows":
                q = ax.quiver(xGrid, yGrid, dx, dy, magnitude, pivot='mid', scale_units='xy', scale=20/(x_range[1]-x_range[0]), cmap='inferno')
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