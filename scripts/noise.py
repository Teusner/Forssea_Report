import numpy as np
from perlin_noise import PerlinNoise
import matplotlib.pyplot as plt

import matplotlib

matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

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

def figure_random():
    global x, y
    global width, heigth
    fig = plt.figure()
    R = np.random.rand(x, y)
    plt.imshow(R)
    plt.tick_params(left = False, right = False , labelleft = False, labelbottom = False, bottom = False)
    fig.set_size_inches(w=width, h=heigth)
    return fig

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
    fig_constant = figure_constant()
    fig_constant.savefig('imgs/pgf/constant.pgf', format='pgf')
    fig_random = figure_random()
    fig_random.savefig('imgs/pgf/random.pgf', format='pgf')
    fig_perlin = figure_perlin()
    fig_perlin.savefig('imgs/pgf/perlin.pgf', format='pgf')
    fig_courant = figure_courant()
    fig_courant.savefig('imgs/pgf/courant.pgf', format='pgf')
