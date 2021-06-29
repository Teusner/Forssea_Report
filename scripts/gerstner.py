import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

# https://en.wikipedia.org/wiki/Trochoidal_wave

g = 9.81
h = 100
m = 4
a_m = np.array([[0.2, 0.1, 0.05, 0.1]])
k_m = np.array([[0.1, 0.05, 0.001, 0.1]])
omega_m = np.sqrt(g*k_m*np.tanh(k_m*h))
phi_m = np.array([[0, 0.2, 0.6, 2]])
h_m = np.array([[0, np.pi/6, np.pi/3, np.pi/9]])

def ksi(alpha, beta, t, a_m, k_m, omega_m, phi_m):
    return alpha - k_m * a_m * np.sin(k_m * alpha - phi_m - omega_m*t)

def eta(alpha, beta, t, a_m, k_m, omega_m, phi_m):
    return a_m * np.cos(k_m * alpha + - phi_m - omega_m * t)

def plot_waves():
    t = 0
    alpha = np.arange(0, 15, 0.001)
    beta = 0

    a_m = np.array([0.1, 1, 1.2])
    k_m = np.array([1, 1, 1])
    omega_m = np.sqrt(g*k_m)
    phi_m = np.array([0, 0, 0])

    fig, axs = plt.subplots(3)
    for i in range(3):
        xi = ksi(alpha, beta, t, a_m[i], k_m[i], omega_m[i], phi_m[i])
        yi = eta(alpha, beta, t, a_m[i], k_m[i], omega_m[i], phi_m[i])
        axs[i].plot(xi, yi, label=r"$a_m \cdot k_m=${}".format(a_m[i]*k_m[i]))
        # axs[i].legend(loc="best")
        axs[i].text(1.7, 0, r"$a_m \cdot k_m=${}".format(a_m[i]*k_m[i]))
        axs[i].grid(True)
    return fig, axs


if __name__ == "__main__":
    fig, axs = plot_waves()
    plt.show()