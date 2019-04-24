import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from math import exp
import numpy as np

def logistisk(t):
    l = lambda x: 1000 / (1 + 100 * exp(-1 * x))
    try:
        len(t)
    except TypeError:
        return l(t)
    else:
        return list(map(l, t))

t = np.linspace(0, 10, 51)

fig, ax = plt.subplots()
ax.plot(t, logistisk(t))
ax.set_yticks([])
ax.set_xticks([])

for r in t[:-1:10]:
    ax.add_patch(Rectangle((r, 0), 2, logistisk(r)))

fig.show()
