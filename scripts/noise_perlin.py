import sys
import numpy as np
from perlin_noise import PerlinNoise
import matplotlib.pyplot as plt

x, y = 100, 100
width = 1.9
heigth = 1.9

def figure_perlin():
    global x, y
    global width, heigth
    fig = plt.figure()
    noise = PerlinNoise(octaves=2, seed=2)
    pic = np.asarray([[noise([i/x, j/y]) for j in range(x)] for i in range(y)])
    plt.imshow(pic[::-1, :])
    plt.tick_params(left = False, right = False , labelleft = False, labelbottom = False, bottom = False)
    fig.set_size_inches(w=width, h=heigth)
    return fig


if __name__ == "__main__":
    args = sys.argv
    if len(args)>1:
        figname = args[1]
    else :
        figname = 'build/imgs/perlin.pdf'
    fig = figure_perlin()
    plt.savefig(figname, format="pdf")
