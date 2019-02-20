import numpy as np
import matplotlib

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

x = np.r_[0.1:30:0.01]
y = 2*np.sin(x)+np.cos(2*x)

fg, ax = plt.subplots()

ax.plot(x, y)

frame_width = 5
step = 0.05
frame_starts = np.r_[0: x[-1] - frame_width: step]
frame_ends = frame_starts + frame_width

pause_time = 0.05

fg.show()
while True:
    for s, e in zip(frame_starts, frame_ends):
        ax.set_xlim([s, e])
        plt.pause(pause_time)
