import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

width, height = 4.5, 3
matplotlib.rcParams.update({'font.size': 9})

def ecart(z, H, k_m):
    return np.linalg.norm((np.cosh(k_m*(z+H)) / np.sinh(k_m*H)- np.exp(k_m*z)) / (np.cosh(k_m*(z+H)) / np.sinh(k_m*H)))


def plot_waves():
    k_m = 1
    H_min = 1
    H_max = 100
    n = 10

    H = np.linspace(H_min, H_max, 100)
    E = []
    for h in H :
        z = np.linspace(-h, 0, n)
        E.append(ecart(z, h, k_m))
    E = np.asarray(E)

    fig, axs = plt.subplots()

    axs.plot(H, E, color="teal")
    axs.grid(True)
    axs.set_ylabel(r"écart relatif (en $\%$)")
    axs.set_xlim(0, H_max)

    fig.set_size_inches(w=width, h=height)
    plt.xlabel(r"H (en $m$)")
    plt.tight_layout()
    return fig, axs


if __name__ == "__main__":
    args = sys.argv
    if len(args)>1:
        figname = args[1]
    else :
        figname = 'build/imgs/simplification_deep_water.pdf'
    fig, axs = plot_waves()
    plt.show()
    # plt.savefig(figname, format="pdf")