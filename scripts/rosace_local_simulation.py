import sys

import bagpy
from bagpy import bagreader

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

import matplotlib
matplotlib.rcParams.update({'font.size': 12})

from scipy.interpolate import interp1d


def figure_rosace():
    # b = bagreader("scripts/rosace_simulation.bag")

    # setpoint = b.message_by_topic('/setpoint')
    # robot_state = b.message_by_topic("/robot_state")

    setpoint = "scripts/rosace_simulation/setpoint.csv"
    df_setpoint = pd.read_csv(setpoint)
    P = [df_setpoint['Time'].to_numpy(), df_setpoint['p.x'].to_numpy(), df_setpoint['p.y'].to_numpy(), df_setpoint['p.z'].to_numpy(), df_setpoint['e.z'].to_numpy()]

    t_h = 0.75*df_setpoint['Time'].to_numpy()
    h = df_setpoint['e.z'].to_numpy()
    f = interp1d(t_h, h, kind="previous", fill_value="extrapolate")

    x0, y0 = -5, 0

    X = df_setpoint['p.x'].to_numpy()[np.newaxis, :] + x0
    Y = df_setpoint['p.y'].to_numpy()[np.newaxis, :] + y0
    T = np.vstack((X, Y))
    R = np.moveaxis(np.array([[np.cos(h), -np.sin(h)], [np.sin(h), np.cos(h)]]), -1, 0)

    Ts = []
    for i in range(T.shape[1]):
        Ts.append(np.array([[np.cos(h[i]), -np.sin(h[i])], [np.sin(h[i]), np.cos(h[i])]]) @ T[:, i])
    Ts = np.asarray(Ts)

    odometry = "scripts/rosace_simulation/robot_state.csv"
    df_odometry = pd.read_csv(odometry)
    tr = 0.75*df_odometry['Time'].to_numpy()[::10]
    Xr = 0.85*df_odometry['p.x'].to_numpy()[np.newaxis, ::10] + x0 + 0.7
    Yr = 0.85*df_odometry['p.y'].to_numpy()[np.newaxis, ::10] + y0 - 0.2

    Tr = np.vstack((Xr, Yr))

    Trobot = []
    for i in range(Tr.shape[1]):
        hr = 1.4*f(tr[i])
        Trobot.append(np.array([[np.cos(hr), -np.sin(hr)], [np.sin(hr), np.cos(hr)]]) @ Tr[:, i])
    Trobot = np.asarray(Trobot)

    fig, ax = plt.subplots()

    points = np.array([Trobot[:, 0], Trobot[:, 1]]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    time = (tr - tr.min())/60

    norm = plt.Normalize(time.min(), time.max())
    lc = LineCollection(segments, cmap='viridis', norm=norm)
    lc.set_array(time)
    lc.set_linewidth(1)

    line = ax.add_collection(lc)
    cbar = fig.colorbar(line, ax=ax)
    cbar.set_label(r'Temps (en $min$)')

    plt.scatter(Ts[:, 0], Ts[:, 1], c=t_h)
    plt.grid(True)
    plt.axis('equal')
    plt.xlabel(r"x (en $m$)")
    plt.ylabel(r"y (en $m$)")
    plt.tight_layout()
    return fig, ax


if __name__ == "__main__":
    args = sys.argv
    if len(args)>1:
        figname = args[1]
    else :
        figname = 'build/imgs/rosace_local_simulation.pdf'
    fig, ax = figure_rosace()
    plt.savefig(figname, format="pdf")
