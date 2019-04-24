from fysikk import g
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch, Rectangle
from math import sin, cos, radians
from matte import fortegn
from numpy import linspace

v_init = 18
theta = 60
epsilon = 1e-8
y_init = 1.7
t0, t1 = (0, 5)
t_gjetning = (t0+t1)/2
verdi = y(t_gjetning)
n = 4
i = 0
plots = dict()
def x(t):
    """x-posisjonen til ballen som en funksjon av tida."""
    return v_init * cos(radians(theta)) * t

def y(t):
    """y-posisjonen til ballen som en funksjon av tida."""
    return -1/2 * g * t**2 + v_init * sin(radians(theta)) * t + y_init
cons = []
while abs(verdi) > epsilon:
    y0 = y(t0)
    y1 = y(t1)
    if i < n:
        plots[i] = [(t0, y0), (t1, y1)]
        if fortegn(verdi) == fortegn(y0):
            cons.append((t_gjetning, t1))
        else:
            cons.append((t0, t_gjetning))
    if fortegn(verdi) == fortegn(y0):
        t0 = t_gjetning
    else:
        t1 = t_gjetning
    t_gjetning = (t0 + t1) / 2
    verdi = y(t_gjetning)
    if i < n:
        plots[i].append((t_gjetning, verdi))
    i += 1

if i >= n:
    plots[i] = [(t0, y(t0)), (t1, y(t1)), (t_gjetning, verdi)]
    cons.append((t0, t1))
   
print(f"Fant løsning ved t = {t_gjetning:.2f},\nlengden på kastet er da {x(t_gjetning):.2f} m")

fig, axs = plt.subplots(n, 1)
fig.suptitle('Halveringsmetoden')
for i, ax in enumerate(axs):
    tmin, tmax = plots[i][0][0], plots[i][1][0]
    ax.set_xlim((tmin, tmax))
    diff = abs(tmax - tmin)
    padd = 0.*diff
    t = linspace(tmin-padd, tmax+padd, 15)
    ax.plot(t, y(t))

for i in range(len(cons)-2):
    tmina, tmaxa = cons[i][0], cons[i][1]
    pmina = (tmina, y(tmina))
    pmaxa = (tmaxa, y(tmaxa))
    # cona = ConnectionPatch(xyA=pmina, xyB=pmina, coordsA="data", coordsB="data",
    #                        axesA=axs[i+1], axesB=axs[i], color='red')
    # conb = ConnectionPatch(xyA=pmaxa, xyB=pmaxa, coordsA="data", coordsB="data",
    #                        axesA=axs[i+1], axesB=axs[i], color='red')
    rect = Rectangle(pmina, width=tmaxa-tmina, height=y(tmaxa)-y(tmina),
                     fill=False, color='red', linestyle='--')
    # axs[i+1].add_artist(cona)
    # axs[i+1].add_artist(conb)
    axs[i].add_artist(rect)
fig.set_facecolor('#ecf0f1')
plt.show()
fig.savefig('../figurer/halveringsmetoden.png', facecolor=fig.get_facecolor())
