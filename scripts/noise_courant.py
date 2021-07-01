import sys
import numpy as np
from perlin_noise import PerlinNoise
import matplotlib.pyplot as plt

x, y = 100, 100
width = 1.9
heigth = 1.9

def figure_courant():
    global x, y
    global width, heigth
    fig = plt.figure()
    noise = PerlinNoise(octaves=2, seed=2)
    pic = [[noise([i/x, j/y]) for j in range(x)] for i in range(y)]
    plt.contourf(pic, alpha=0.7)
    dy, dx = np.gradient(pic)
    plt.streamplot(np.arange(0, x, 1), np.arange(0, y, 1), dx, dy, color='black', density=1, linewidth=0.5)
    plt.tick_params(left = False, right = False , labelleft = False, labelbottom = False, bottom = False)
    fig.set_size_inches(w=width, h=heigth)
    return fig


if __name__ == "__main__":
    args = sys.argv
    if len(args)>1:
        figname = args[1]
    else :
        figname = 'build/imgs/courant.pdf'
    fig = figure_courant()
    plt.savefig(figname, format="pdf")
