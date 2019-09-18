n = input(">>> Hvilket tall vil du ha kvadratroten av? ")
n = float(n)

epsilon = 1E-7     # Betyr 1 * 10 ^-7


# Gjør en initiell gjetning
a = 1

while abs(a ** 2 - n) > epsilon:
    # Vi gjør en oppdatering av gjetningen vår
    a = (a + n/a) / 2

# Når programmet er ferdig, inneholder 'a' svaret
print(f"Kvadratroten av {n} er {a}.")
