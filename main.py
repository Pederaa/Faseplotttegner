from plotter import plotter

# Defining the differential system to plot
def system(t, z):
    x, y = z

    dx = (y-x)*(y+x)
    dy = x*(x+1)
    return [dx, dy]


if __name__ == "__main__":
    pl = plotter()
    pl.draw(system)