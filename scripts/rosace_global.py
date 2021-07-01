import bagpy
from bagpy import bagreader

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm


if __name__ == "__main__":

    # b = bagreader('scripts/rosace.bag')

    # print(b.topic_table)
    # odometry = b.message_by_topic('/odometry/robot_state')
    odometry = "scripts/rosace/odometry-robot_state.csv"
    df_odometry = pd.read_csv(odometry)
    R = [df_odometry['Time'].to_numpy(), df_odometry['p.x'].to_numpy(), df_odometry['p.y'].to_numpy(), df_odometry['p.z'].to_numpy(), df_odometry['e.z'].to_numpy()]

    # fig, axs = plt.subplots(4, sharex=True)
    # for i in range(4):
    #     axs[i].plot(R[0], R[i+1])

    # plt.figure()
    # plt.plot(R[1], R[2])
    # plt.show()

    # setpoint = b.message_by_topic('/stacks/dynamic_positioning/setpoint')
    setpoint = "scripts/rosace/stacks-dynamic_positioning-setpoint.csv"
    df_setpoint = pd.read_csv(setpoint)
    P = [df_setpoint['Time'].to_numpy(), df_setpoint['p.x'].to_numpy(), df_setpoint['p.y'].to_numpy(), df_setpoint['p.z'].to_numpy(), df_setpoint['e.z'].to_numpy()]

    # fig, axs = plt.subplots(4, sharex=True)
    # for i in range(4):
    #     axs[i].plot(P[0], P[i+1])


    fig, ax = plt.subplots()

    points = np.array([R[1], R[2]]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    time = (R[0] - R[0].min())/60

    norm = plt.Normalize(time.min(), time.max())
    lc = LineCollection(segments, cmap='viridis', norm=norm)
    lc.set_array(time)
    lc.set_linewidth(1)

    line = ax.add_collection(lc)
    cbar = fig.colorbar(line, ax=ax)
    cbar.set_label(r'Temps (en $min$)')

    plt.scatter(P[1], P[2], color='crimson')
    plt.grid(True)
    plt.axis('equal')
    plt.xlabel(r"x (en $m$)")
    plt.ylabel(r"y (en $m$)")
    plt.show()
