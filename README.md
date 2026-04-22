# Phaseplottdrawer script
This is a script that can numerically draw the phaseplot of any 2D system of differential equations. Was orgininally made as a way to test the solutions to the course [TMA4160](https://www.ntnu.edu/studies/courses/TMA4165/2018/1#tab=omEmnet) at NTNU. 
The script uses the scipy.integrate and numpy libraries for numrical analysis and the matplotlib library to plot the results. 
  

# Running the script
For running this script, open the 'main.py' script and edit the system(x, y)-function. it is by default set to:

```
    def system(t, z):
        x, y = z

        dx = (y-x)*(y+x)
        dy = x*(x+1)
        return [dx, dy]
```

Replace 'dx = ...' and 'dy = ...' with your equations of state, and run the 'main.py' script either in your IDE of choice, or in the terminal with the command 'python3 main.py'. 


# Future ideas:
- Look into using SymPy for the equations of state. Might make it easier to work with
- Make a script that calculates the eqv. points of the system and scales the graph automatically to include them. the case of infinite eqv. points will have to be dealt with. 
- Make the script able to classify eqv. points. Should be simple for non-marginaly stable points, linearization should be sufficient according to the [Hartman-Grobman Theorem](https://en.wikipedia.org/wiki/Hartman%E2%80%93Grobman_theorem). For marginally stable ones, it is more difficult. 
- Make the script into a pythonpackage that can be easily run by others. 
- Expand to 3D systems
