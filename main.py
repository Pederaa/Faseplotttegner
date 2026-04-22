import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
import math

# Defining the differential system to plot
def system(t, z):
    x, y = z

    dx = (y-x)*(y+x)
    dy = x*(x+1)
    return [dx, dy]


# Make the grid
x_range = [-3, 3]
y_range = [-3, 3]
n = 40
x, y = np.meshgrid( np.linspace(x_range[0], x_range[1], n), 
                    np.linspace(y_range[0], y_range[1], n)
            )


# Calculate the derivatives at every point on the grid and scale them down
dx, dy = system(0, [x, y])
magnitude = np.sqrt(dx**2 + dy**2)
dx, dy = dx/magnitude, dy/magnitude


# Draw the graph
fig, ax = plt.subplots()

# Solve and plot trajectories from various starting points
#initial_conditions = [(1/np.pi, 0), (1/(2*np.pi), 0), (1/(3*np.pi), 0), (1/(4*np.pi), 0)]
#t_span = [0, 20]
#t_eval = np.linspace(*t_span, 1000)

#for x0, y0 in initial_conditions:
#    sol = solve_ivp(system, t_span, [x0, y0], t_eval=t_eval)
#    ax.plot(sol.y[0], sol.y[1])


# Plots everytning in a plot
q = ax.quiver(x, y, dx, dy, magnitude, pivot='mid', scale_units='xy', scale=2*20/(x_range[1]-x_range[0]), cmap='inferno')


ax.set_xlim(x_range)
ax.set_ylim(y_range)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Phase portrait')

plt.grid(True)
plt.colorbar(q)
#ax.legend()
plt.show()