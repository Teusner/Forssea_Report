import sys
import numpy as np
from perlin_noise import PerlinNoise
import matplotlib.pyplot as plt

x, y = 100, 100
width = 1.9
heigth = 1.9

def figure_random():
    global x, y
    global width, heigth
    fig = plt.figure()
    R = np.random.rand(x, y)
    plt.imshow(R)
    plt.tick_params(left = False, right = False , labelleft = False, labelbottom = False, bottom = False)
    fig.set_size_inches(w=width, h=heigth)
    return fig


if __name__ == "__main__":
    args = sys.argv
    if len(args)>1:
        figname = args[1]
    else :
        figname = 'build/imgs/random.pdf'
    fig = figure_random()
    plt.savefig(figname, format="pdf")
