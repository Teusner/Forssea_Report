import sys
import numpy as np
import matplotlib.pyplot as plt

width, height = 4.5, 3

# https://en.wikipedia.org/wiki/Trochoidal_wave

def ksi(alpha, beta, t, a_m, k_m, omega_m, phi_m):
    return alpha - k_m * a_m * np.sin(k_m * alpha - phi_m - omega_m*t)

def eta(alpha, beta, t, a_m, k_m, omega_m, phi_m):
    return a_m * np.cos(k_m * alpha + - phi_m - omega_m * t)

def plot_waves():
    t = 0
    alpha = np.arange(0, 15, 0.001)
    beta = 0

    g = 9.81
    a_m = np.array([0.1, 1, 1.2])
    k_m = np.array([1, 1, 1])
    omega_m = np.sqrt(g*k_m)
    phi_m = np.array([0, 0, 0])

    fig, axs = plt.subplots(3, sharex=True)
    for i in range(3):
        xi = ksi(alpha, beta, t, a_m[i], k_m[i], omega_m[i], phi_m[i])
        yi = eta(alpha, beta, t, a_m[i], k_m[i], omega_m[i], phi_m[i])
        axs[i].plot(xi, yi)
        axs[i].text(1.7, 0, r"$a_mk_m=${}".format(a_m[i]*k_m[i]), fontsize=9)
        axs[i].grid(True)
        axs[i].set_ylabel(r"z (en $m$)")
        axs[i].fill_between(xi, yi, -1.2*a_m[i]*np.ones(yi.shape), color="teal", alpha=0.5)
    fig.set_size_inches(w=width, h=height)
    plt.xlabel(r"x (en $m$)")
    plt.tight_layout()
    return fig, axs


if __name__ == "__main__":
    args = sys.argv
    if len(args)>1:
        figname = args[1]
    else :
        figname = 'build/imgs/gerstner_wave.pdf'
    fig, axs = plot_waves()
    plt.savefig(figname, format="pdf")