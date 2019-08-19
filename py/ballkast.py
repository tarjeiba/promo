########################################################################
# Vi skal finne ut hvor langt en ball blei kastet. Ballen vil da følge #
# en parameterframstilling som gitt under.                             #
#                                                                      #
# y(t) = -1/2 * g * t ** 2 + v_0 * sin(theta) * t + y_0                #
# x(t) = v_0 * cos(theta) * t                                          #
########################################################################


from math import radians, cos, sin
from matte import fortegn

v_init = 18        # startfarten i m/s
theta = 60     # utgangsvinkel i grader fra horisontalplanet
g = 9.81       # tyngdeakselerasjonen i m/s**2
y_init = 1.7       # starthøyden til ballen
epsilon = 1e-2 # hva godtar vi som "godt nok"?

def x(t):
    """x-posisjonen til ballen som en funksjon av tida."""
    return v_init * cos(radians(theta)) * t

def y(t):
    """y-posisjonen til ballen som en funksjon av tida."""
    return -1/2 * g * t**2 + v_init * sin(radians(theta)) * t + y_init


# Likningsløsnig

# Numerisk løsning

# Halveringsmetoden
t0, t1 = (0, 5)
t_gjetning = (t0+t1)/2
verdi = y(t_gjetning)

while abs(verdi) > epsilon:
    y0 = y(t0)
    y1 = y(t1)
    if fortegn(verdi) == fortegn(y0):
        t0 = t_gjetning
    else:
        t1 = t_gjetning
    t_gjetning = (t0 + t1) / 2
    print(t_gjetning)
    verdi = y(t_gjetning)

print(f"Fant løsning ved t = {t_gjetning:.2f},\nlengden på kastet er da {x(t_gjetning):.2f} m")


# Modellering
v = radians(60)                     # utgangsvinkelen i radianer
xpos, ypos = (0, 1.7)               # initialbetingelser
vx, vy = (18 * cos(v), 18 * sin(v)) # fart
ax, ay = (0, -9.81)                 # akselarasjon
t = 0.0                             # starttid
tslutt = 5.0                        # termineringsbetingelse
delta_t = 0.01
posisjoner = [(xpos, ypos)]

while ypos > 0:
    xpos += vx * delta_t
    ypos += vy * delta_t
    posisjoner.append((xpos, ypos))
    if ypos < 0:
        break
    vx += ax * delta_t
    vy += ay * delta_t
    t += delta_t

print(f"Fant løsning ved t = {t:.2f}\nlengden på kastet er da {xpos:.2f} m")

# Modellering ulike Δt
import matplotlib.pyplot as plt

c = v = radians(60)                     # utgangsvinkelen i radianer
posisjoner = dict()
delta_ter = [0.0001, 0.001, 0.01, 0.1, 1]

for delta_t in delta_ter:
    xpos, ypos = (0, 1.7)               # initialbetingelser
    vx, vy = (18 * cos(v), 18 * sin(v)) # fart
    ax, ay = (0, -9.81)                 # akselarasjon
    posisjoner[delta_t] = [(xpos, ypos)]

    while ypos > 0:
        xpos += vx * delta_t
        ypos += vy * delta_t
        posisjoner[delta_t].append((xpos, ypos))
        vx += ax * delta_t
        vy += ay * delta_t

for delta_t in posisjoner:
    plt.plot([pos[0] for pos in posisjoner[delta_t]], [pos[1] for pos in posisjoner[delta_t]], label="Δt = "+str(delta_t))
    plt.legend()
    plt.ylabel("høyde (m)")
    plt.xlabel("x-posisjon (m)")
    plt.title("Sammenligning av ulike verdier av Δt")

plt.show()
