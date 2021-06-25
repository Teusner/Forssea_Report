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

def ksi(alpha, beta, t):
    return alpha - np.sum(np.cos(h_m) * k_m * a_m / np.tanh(k_m*h) * np.sin(alpha[:, :, np.newaxis]@(np.cos(h_m)*k_m) + beta[:, :, np.newaxis]@(np.sin(h_m)*k_m) - np.ones(alpha[:, :, np.newaxis].shape)@(phi_m+omega_m*t) + 10*np.repeat(zeta(alpha, beta, t)[:, :, np.newaxis], m, axis=2)), axis=2)

def eta(alpha, beta, t):
    return beta - np.sum(np.sin(h_m) * k_m * a_m / np.tanh(k_m*h) * np.sin(alpha[:, :, np.newaxis]@(np.cos(h_m)*k_m) + beta[:, :, np.newaxis]@(np.sin(h_m)*k_m) - np.ones(alpha[:, :, np.newaxis].shape)@(phi_m+omega_m*t) + 10*np.repeat(zeta(alpha, beta, t)[:, :, np.newaxis], m, axis=2)), axis=2)

def zeta(alpha, beta, t):
    return np.sum(a_m * np.cos(alpha[:, :, np.newaxis]@(np.cos(h_m)*k_m) + beta[:, :, np.newaxis]@(np.sin(h_m)*k_m) - np.ones(alpha[:, :, np.newaxis].shape)@(phi_m+omega_m*t)), axis=2)


if __name__ == "__main__":
    t = np.arange(0, 30, 0.5)
    alpha = np.arange(-100, 100, 2)
    beta = np.arange(-100, 100, 2)
    Alpha, Beta = np.meshgrid(alpha, beta)

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.set_title('Surface plot')

    for T in t:
        x = ksi(Alpha, Beta, T)
        y = eta(Alpha, Beta, T)
        z = zeta(Alpha, Beta, T)

        ax.clear()
        ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')

        plt.pause(0.0001)    
    