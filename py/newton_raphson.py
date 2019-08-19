from matte import derivert_framover_euler, lineaert_nullpunkt

def newton_raphson(f, a, dx=0.00001, eps=0.00001):
    """Returnerer et av de eventuelle nullpunktene til f med initiell gjetning
    x = a. abs(f(nullpunkt)) < eps.
    """

    while abs(f(a)) > eps:
        der = derivert_framover_euler(f, a, dx)
        a = lineaert_nullpunkt(der, f(a), a)
    return a
