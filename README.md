# Phaseplottdrawer script
This is a script that can numerically draw the phaseplot of any 2D system of differential equations of the form $\dot{x} = f(x)$, $x \in \R^2$ . Was orgininally made as a way to test the solutions to the course [TMA4160](https://www.ntnu.edu/studies/courses/TMA4165/2018/1#tab=omEmnet) at NTNU. 

The script relies on the SymPy library, and requires the input to follow this format. It also uses the scipy.integrate and numpy libraries for numrical analysis and the matplotlib library to plot the results. 


# Running the script
For running this script, open the 'main.py' script and edit the diffEquations-initialization. It is by default set to:

```
sys = diffEquations(
    dx = (y-x)*(y+x),
    dy = x*(x+1)
)
```

Replace 'dx = ...' and 'dy = ...' with your equations of state, and run the 'main.py' script either in your IDE of choice, or in the terminal with the command 'python3 main.py'. 


# Future ideas:
- Make a script that calculates the eqv. points of the system and scales the graph automatically to include them. the case of infinite eqv. points will have to be dealt with. 
- Make the script able to classify eqv. points. Should be simple for non-marginaly stable points, linearization should be sufficient according to the [Hartman-Grobman Theorem](https://en.wikipedia.org/wiki/Hartman%E2%80%93Grobman_theorem). For marginally stable ones, it is more difficult. 
- Make the script into a pythonpackage that can be easily run by others. 
- Expand the code to accept 3D systems
- Expand the code to accept 1D systems
- Make animations