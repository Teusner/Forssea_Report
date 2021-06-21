import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation


def wave(r, k, omega):
    x = x0 + r * np.sin(k*x0 - omega*t)
    z = z0 - r * np.cos(k*x0 - omega*t)
    return x, z

# https://en.wikipedia.org/wiki/Trochoidal_wave

g = 9.81
h = 100
m = 3
a_m = np.array([1, 0.5, 0.25]).reshape((3, 1))
k_m = np.array([1, 0.5, 0.25]).reshape((3, 1))
omega_m = np.sqrt(g*k_m*np.tanh(k_m*h))
phi_m = np.array([0, 0, 0]).reshape((3, 1))

def ksi(alpha, beta, t):
    return alpha - np.sum(a_m / np.tanh(k_m*h) * np.sin(k_m * alpha - omega_m * t - phi_m * np.ones(t.shape)), axis=0)


if __name__ == "__main__":
    t = np.arange(0, 20, 0.1)
    alpha = np.arange(-10, 10, 0.1)
    beta = np.arange(-10, 10, 0.1)
    Alpha, Beta = np.meshgrid(alpha, beta)

    x = ksi(alpha, beta, t)

    plt.figure()
    plt.plot(t, x)
    plt.show()


    # # Required parameters
    # r = 1
    # k = 5.5
    # omega = 1

    # # Parameters computing
    # H = 2*r
    # L = 2*np.pi/k
    # T = 2*np.pi/omega
    # c = omega/k

    # print(f"Celerity {c=}")
    # print(f"{k*r=}")

    # x = x0 + r * np.sin(k*x0 - omega*t)
    # z = z0 - r * np.cos(k*x0 - omega*t)

    # #  t=0
    # # alpha = -k*x0
    # # x = -alpha/k - r*np.sin(alpha)
    # # z = r*np.cos(alpha)

    # # fig, (ax1, ax2) = plt.subplots(2, 1)
    # # ax1.plot(t, x)
    # # ax2.plot(t, z)

    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # wave_plot, = plt.plot(x, z)
    # ax.grid(True)
    # ax.set_aspect('equal')

    # k_slider_ax = plt.axes([0.1, 0.05, 0.8, 0.05])
    # r_slider_ax = plt.axes([0.1, 0.15, 0.8, 0.05])
    # k_slider = Slider(k_slider_ax, 'k', 0.1, 10, valinit=5.5)
    # r_slider = Slider(r_slider_ax, 'r', 0.1, 10, valinit=1)
    # plt.title(f"Wave {r*k=}")

    # def update(val):
    #     global x, z, r, k, H, L
    #     r, k = r_slider.val, k_slider.val
    #     H = 2*r
    #     L = 2*np.pi/k
    #     x = x0 + r * np.sin(k*x0 - omega*t)
    #     z = z0 - r * np.cos(k*x0 - omega*t)
    #     wave_plot.set_xdata(x)
    #     wave_plot.set_ydata(z)
    #     plt.title(f"Wave {r*k=} {H/L=}")
    #     ax.axis([np.min(x), np.max(x), np.min(z), np.max(z)])
    #     fig.canvas.draw_idle()

    # k_slider.on_changed(update)
    # r_slider.on_changed(update)

    # plt.show()

    
    