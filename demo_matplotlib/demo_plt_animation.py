import numpy as np
import scipy.constants
import matplotlib

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation

turns_per_second = 0.3
radians_per_second = turns_per_second * np.pi * 2

radius_per_turn = scipy.constants.golden
zoom_factor = 2

interval = 10 / 1000
intervals_per_turn = 1 / (turns_per_second * interval)
radius_per_interval = radius_per_turn ** (1 / intervals_per_turn)


def data_gen(start=(0, 1), time_limit=5):
    angle, radius = start
    t = 0
    while True:
        yield angle, radius
        t += interval
        if t >= time_limit:
            break
        angle += interval * radians_per_second
        radius *= radius_per_interval


def init():
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    return line,


fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []


def run(data):
    # update the data
    angle, radius = data
    x, y = np.cos(angle) * radius, np.sin(angle) * radius
    xdata.append(x)
    ydata.append(y)
    _, xmax = ax.get_xlim()
    if xmax < max(abs(x), abs(y)):
        xmax *= zoom_factor
        ax.set_xlim(-xmax, xmax)
        ax.set_ylim(-xmax, xmax)

    line.set_data(xdata, ydata)

    return line,


ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=interval * 1000,
                              repeat=True, init_func=init)
plt.show()
