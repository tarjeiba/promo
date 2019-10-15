"""Dette programmet regner ut den deriverte av en enkel matematisk funksjon
ved å å bruke en egen derivasjonsfunksjon.

Laget av Tarjei
"""
import math

def derivert_av_funk_ved_x(funksjon, x):
    """Returnerer den numeriske verdien av den deriverte av funksjonen
    'funksjon' når x er 'x'.

    Bruk en 'framoverdifferanse' (se forrige oppgave) med 'delta_x = 0.0001'.

    Eksempel:
    def f(x):
        return x ** 2

    >>> derivert_av_funk_ved_x(f, 2)   =>  4.0001000000078335

    """
    delta_x = 0.0001
    return (funksjon(x + delta_x) - funksjon(x)) / delta_x


# Vi kan nå teste funksjonen for de samme verdiene av x, med vår gamle f

def f(x):
    return 3 * x ** 2 * math.log10(x) - 15

x = 20
print("   x     --     f(x)     --     f'(x)")
print("-------------------------------------")
while x <= 29:
    f_av_x = f(x)
    der_av_f_ved_x = derivert_av_funk_ved_x(f, x)
    print(f"{x}    --    {f_av_x:.1f}    --    {der_av_f_ved_x:.2f}")
    x += 1
