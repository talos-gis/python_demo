import numpy as np
import scipy.constants
import matplotlib

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation

interval = 5 / 1000
zoom_factor = 1.5

radii = np.array([5, 1, 0.5])
turn_speeds = np.array([1 / 10, 1 / 4.2, 1]) * 4
turn_duration = 1 / turn_speeds
radians_per_interval = (np.pi * 2 * interval) / turn_duration
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
x_data, y_data = [], []


def calc_marker(radii, angles):
    x_o = np.cos(angles)*radii
    y_o = np.sin(angles)*radii

    return np.sum(x_o), np.sum(y_o)


def data_gen(full_turns=1, time_to_end=5):
    angles = np.zeros_like(radians_per_interval)
    zeros = angles.copy()
    fulls = zeros + 2 * np.pi
    color = (0.5, 0.5, 0.8)
    while True:
        x, y = calc_marker(radii, angles)
        yield x, y, color
        color = None
        angles += radians_per_interval
        angles %= (2 * np.pi)
        if np.all(np.isclose(angles, zeros)
                  | np.isclose(angles, fulls)):
            full_turns -= 1
            color = (0.5, 0.7, 0.5)
        if full_turns <= 0:
            time_to_end -= interval
            if time_to_end <= 0:
                break


def init():
    del x_data[:]
    del y_data[:]
    line.set_data(x_data, y_data)
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    return line,


def run(data):
    # update the data
    x, y, color = data
    x_data.append(x)
    y_data.append(y)
    _, xmax = ax.get_xlim()
    if xmax < max(abs(x), abs(y)):
        xmax *= zoom_factor
        ax.set_xlim(-xmax, xmax)
        ax.set_ylim(-xmax, xmax)

    line.set_data(x_data, y_data)
    if color:
        line.set_color(color)

    return line,


ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=interval * 1000,
                              repeat=True, init_func=init)
plt.show()
