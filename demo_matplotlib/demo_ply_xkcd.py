import numpy as np
import matplotlib

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

plt.xkcd(randomness=2, scale=1.5)

fig = plt.figure()
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.xticks([])
plt.yticks([])
plt.ylim([-3, 8])

data = np.array([(0, 0), (2, 1), (4, 6), (5, 6.5), (6, -2)])

plt.plot(data[:, 0], data[:, 1])

plt.annotate(
    'plt is a dumb\nabbreviation',
    xy=(0, 0), arrowprops=dict(arrowstyle='->'), xytext=(0, -2))

plt.annotate(
    'freestyle fooling\naround',
    xy=(2, 1), arrowprops=dict(arrowstyle='->'), xytext=(4, 0),
    horizontalalignment='center')

plt.annotate(
    'read\nexamples\nonline',
    xy=(4, 6), arrowprops=dict(arrowstyle='->'), xytext=(2.5, 6),
    horizontalalignment='center')

plt.annotate(
    "THERE'S AN\nXKCD STYLE?!",
    xy=(5, 6.5), arrowprops=dict(arrowstyle='->'), xytext=(5, 7.5),
    horizontalalignment='center')

#plt.xlabel('time')
plt.ylabel('how useful my graphs are')

plt.show()
