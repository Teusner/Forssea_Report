import sys
import numpy as np
from perlin_noise import PerlinNoise
import matplotlib.pyplot as plt

x, y = 100, 100
width = 1.9
heigth = 1.9

def figure_constant():
    global x, y
    global width, heigth
    fig = plt.figure()
    X, Y = np.meshgrid(np.arange(0, x, 10), np.arange(0, y, 10))
    theta = np.pi/2 - np.pi/3
    U = np.cos(theta)*np.ones(X.shape)
    V = np.sin(theta)*np.ones(Y.shape)
    plt.quiver(X, Y, U, V, scale=9)
    plt.tick_params(left = False, right = False , labelleft = False, labelbottom = False, bottom = False)
    fig.set_size_inches(w=width, h=heigth)
    return fig


if __name__ == "__main__":
    args = sys.argv
    if len(args)>1:
        figname = args[1]
    else :
        figname = 'build/imgs/constant.pdf'
    fig = figure_constant()
    plt.savefig(figname, format="pdf")