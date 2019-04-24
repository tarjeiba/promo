import math

def radianer_til_grader(vinkel):
    """Tar inn en vinkel gitt i radianer, og returnerer den samme i grader."""
    return 180 / math.pi * vinkel

def abc(a, b, c):
    d = b ** 2 - 4 * a * c
    if d == 0:
        return [-b / (2*a)]
    elif d > 0:
        return [(-b - math.sqrt(d)) / (2*a) , (-b + math.sqrt(d)) / (2*a)]
    else:
        print("Likningen har ingen reelle løsninger.")
        return None

def derivert_framover_euler(f, a, dx=0.0001):
    """Returnerer den deriverte av f i a utregnet med en framover-euler med dx."""
    return (f(a + dx) - f(a)) / dx

def lineaert_nullpunkt(a, fa, x0=0):
    """Returnerer nullpunktet til y = a x + b. Via ettpunktsformelen, kan vi da få
    nullpunktet, y = 0, gitt som x0 - fa/a
    """
    return x0 - fa/a

def fortegn(n):
    if n < 0:
        return -1
    if n >= 0:
        return 1
