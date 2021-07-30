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

def figure_rosace_global():
    odometry = "scripts/rosace_simulation/robot_state.csv"
    df_odometry = pd.read_csv(odometry)
    R = [3/5*df_odometry['Time'].to_numpy()[::1000], df_odometry['p.x'].to_numpy()[::1000], df_odometry['p.y'].to_numpy()[::1000], df_odometry['p.z'].to_numpy()[::1000], df_odometry['e.z'].to_numpy()[::1000]]

    setpoint = "scripts/rosace_simulation/setpoint.csv"
    df_setpoint = pd.read_csv(setpoint)
    P = [3/5*df_setpoint['Time'].to_numpy(), df_setpoint['p.x'].to_numpy(), df_setpoint['p.y'].to_numpy(), df_setpoint['p.z'].to_numpy(), df_setpoint['e.z'].to_numpy()]

    fig, ax = plt.subplots()

    x0, y0 = -5, 0

    points = np.array([R[1] + x0, R[2] + y0]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    time = (R[0] - R[0].min())/60

    norm = plt.Normalize(time.min(), time.max())
    lc = LineCollection(segments, cmap='viridis', norm=norm)
    lc.set_array(time)
    lc.set_linewidth(1)

    line = ax.add_collection(lc)
    cbar = fig.colorbar(line, ax=ax)
    cbar.set_label(r'Temps (en $min$)')

    plt.scatter(P[1] + x0, P[2] + y0, color='crimson')
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
        figname = 'build/imgs/rosace_global_simulation.pdf'
    fig, ax = figure_rosace_global()
    plt.savefig(figname, format="pdf")
