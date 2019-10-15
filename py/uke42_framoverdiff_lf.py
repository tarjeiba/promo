"""Dette programmet regner ut den deriverte av en enkel matematiske funksjon
ved en del ulike x-verdier.

Laget av Tarjei
"""

import math

def f(x):
    return 3 * x ** 2 * math.log10(x) - 15

delta_x = 0.001    # velger en veldig liten verdi for delta x
eval_x = 4
delta_f = f(eval_x + delta_x) - f(eval_x)

derivert = delta_f / delta_x

print(f"Den deriverte av funksjonen ved x = {eval_x} er omtrent {derivert:.2f}.")

x = 20
print("   x     --     f(x)     --     f'(x)")
print("-------------------------------------")
while x <= 29:
    f_av_x = f(x)
    der_av_f_ved_x = (f(x+delta_x) - f(x)) / delta_x
    print(f"{x}    --    {f_av_x:.1f}    --    {der_av_f_ved_x:.2f}")
    x += 1
