import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 9})

width, height = 7, 3

# https://en.wikipedia.org/wiki/Trochoidal_wave

def ksi(alpha, beta, t, a_m, k_m, omega_m, phi_m):
    return alpha - k_m * a_m * np.sin(k_m * alpha - phi_m - omega_m*t)

def eta(alpha, beta, t, a_m, k_m, omega_m, phi_m):
    return a_m * np.cos(k_m * alpha + - phi_m - omega_m * t)

def ds_dalpha(alpha, beta, z, t, a_m, k_m, omega_m, phi_m, h_m):
    ds = np.zeros(3)
    theta_m = (np.cos(h_m) * alpha + np.sin(h_m) * beta) * k_m - omega_m*t - phi_m
    ds[0] = 1 - a_m * k_m * np.cos(h_m)**2 * np.cos(theta_m)
    ds[1] = - a_m * k_m * np.sin(h_m) * np.cos(h_m) * np.cos(theta_m)
    ds[2] = - a_m * k_m * np.cos(h_m) * np.sin(theta_m)
    return ds

def ds_dbeta(alpha, beta, z, t, a_m, k_m, omega_m, phi_m, h_m):
    ds = np.zeros(3)
    theta_m = (np.cos(h_m) * alpha + np.sin(h_m) * beta) * k_m - omega_m*t - phi_m
    ds[0] = - a_m * k_m * np.sin(h_m) * np.cos(h_m) * np.cos(theta_m)
    ds[1] = 1 - a_m * k_m * np.sin(h_m)**2 * np.cos(theta_m)
    ds[2] = - a_m * k_m * np.sin(h_m) * np.sin(theta_m)
    return ds

def plot_waves():
    t = 0
    alpha = np.arange(0, 20, 0.001)
    beta = 0

    # Arrows processing
    A = np.arange(0, 20.1, 1.5)
    b = 0
    Z = np.arange(-4, 1, 1.5)

    g = 9.81
    a_m = 1
    k_m = 0.6
    omega_m = np.sqrt(g*k_m)
    phi_m = 0
    h_m = 0

    fig, ax = plt.subplots()
    xi = ksi(alpha, beta, t, a_m, k_m, omega_m, phi_m)
    yi = eta(alpha, beta, t, a_m, k_m, omega_m, phi_m)
    ax.plot(xi, yi)
    ax.fill_between(xi, yi, -4*a_m*np.ones(yi.shape), color="teal", alpha=0.5)

    for a in A:
        for z in Z:
            water_level = z - eta(a, beta, t, a_m, k_m, omega_m, phi_m)
            if water_level < a_m / 2 * np.cos(k_m * a + - phi_m - omega_m * t) - 1:
                n = np.cross(ds_dalpha(a, b, water_level, t, a_m, k_m, omega_m, phi_m, h_m), ds_dbeta(a, b, water_level, t, a_m, k_m, omega_m, phi_m, h_m))
                n = np.exp(k_m*water_level) * n + np.array([0, 0, 1])
                ax.quiver(a, z, n[0], n[2])

    alpha = np.arange(0, 20, 0.8)
    beta = 0
    xi = ksi(alpha, beta, t, a_m, k_m, omega_m, phi_m)
    yi = eta(alpha, beta, t, a_m, k_m, omega_m, phi_m)
    for i in range(len(xi)):
        n = np.cross(ds_dalpha(xi[i], b, yi[i], t, a_m, k_m, omega_m, phi_m, h_m), ds_dbeta(xi[i], b, yi[i], t, a_m, k_m, omega_m, phi_m, h_m))
        ax.quiver(xi[i], yi[i], n[0], n[2])

    ax.set_ylabel(r"z (en $m$)")
    plt.xlabel(r"x (en $m$)")
    ax.grid(True)
    ax.set_ylim(-4, 2)

    fig.set_size_inches(w=width, h=height)
    plt.tight_layout()
    return fig, ax


if __name__ == "__main__":
    args = sys.argv
    if len(args)>1:
        figname = args[1]
    else :
        figname = 'build/imgs/gerstner_normal.pdf'
    fig, ax = plot_waves()
    plt.show()
    # plt.savefig(figname, format="pdf")