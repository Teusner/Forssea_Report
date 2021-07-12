import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

width, height = 4.5, 3
matplotlib.rcParams.update({'font.size': 9})

def u(alpha, beta, z, t, a_m, k_m, omega_m, phi_m, H):
    return - a_m * omega_m * np.cosh(k_m*(z+H)) / np.sinh(k_m*H) * np.cos(k_m * alpha - phi_m - omega_m * t)

def p(alpha, beta, z, t, a_m, k_m, omega_m, phi_m, H, rho, g):
    return rho * a_m * omega_m**2 * np.cosh(k_m*(z+H)) / np.sinh(k_m*H) * np.cos(k_m * alpha - phi_m - omega_m * t) - rho*g*z

def plot_waves():
    alpha, beta, t = 0, 0, 0
    H = 10
    z = np.arange(-H, 0, 0.001)

    g = 9.81
    a_m = 1
    k_m = 1
    omega_m = np.sqrt(g*k_m)
    phi_m = 0
    rho = 1030

    fig, axs = plt.subplots(2, sharex=True)

    # Velocity
    axs[0].plot(-z, 0 * z, color="crimson", label="Vitesse sans vagues")
    axs[0].plot(-z, u(alpha, beta, z, t, a_m, k_m, omega_m, phi_m, H), color="teal", label="Vitesse avec vagues")
    axs[0].grid(True)
    axs[0].set_ylabel(r"vitesse (en $m.s^{-1}$)")
    axs[0].set_xlim(0, H)
    axs[0].legend(loc="lower right")

    axs[1].plot(-z, - rho * g * z / 1e5, color="crimson", label="Pression sans vagues")
    axs[1].plot(-z, p(alpha, beta, z, t, a_m, k_m, omega_m, phi_m, H, rho, g) / 1e5, color="teal", label="Pression avec vagues")
    axs[1].grid(True)
    axs[1].set_xlim(0, H)
    axs[1].set_ylabel(r"pression (en $bar$)")
    axs[1].legend(loc="lower right")


    fig.set_size_inches(w=width, h=height)
    plt.xlabel(r"profondeur (en $m$)")
    plt.tight_layout()
    return fig, axs


if __name__ == "__main__":
    args = sys.argv
    if len(args)>1:
        figname = args[1]
    else :
        figname = 'build/imgs/gerstner_velocity_pressure_depth.pdf'
    fig, axs = plot_waves()
    plt.savefig(figname, format="pdf")