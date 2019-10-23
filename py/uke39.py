""" Dette programmet bruker halveringsmetoden til å løse likninga

x ** 3 + 5 = 5x, som da er endret til
x ** 3 - 5x + 5 = 0

Det er skrevet av Tarjei, 25. september 2019.
"""


# Spoileralert for resten av faget

def f(x):
    return x ** 3 - 5*x + 5
 
# Vi kan nå regne ut f(3), for eksempel

x1 = -5
x2 = 3

epsilon = 1e-7   # 0.0000001

while abs(x2 - x1) > epsilon:
    middelverdi = (x1 + x2) / 2
    if f(middelverdi) > 0:
        x2 = middelverdi
    elif f(middelverdi) < 0:
        x1 = middelverdi
    elif f(middelverdi) == 0:
        x1 = middelverdi
        break

print(f"Svaret ditt er {x1:.2f}.")
