"""
Collatz' formodning sier at om vi følger den iterative prosessen 

n <- n / 2 hvis n er et partall
n <- 3* + 1 hvis n er et oddetall

Vil alltid n ende på 1. 

Dette er en enkelt påstand, som det ikke er opplagt at alltid vil stemme.

Tilleggsutfordring
Hvilken startverdi under 10000 gir den lengste sekvensen av tall før den stabiliserer seg på 1?

Starter vi for eksempel med n = 7, får vi følgende sekvens:
7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1

Med startverdi på 7, får vi altså 17 verdier før vi er på 1.

"""

#################
# Enkel løsning #
#################

n = 7

# Ønsker å sjekke om n er partall
while n != 1:
    print(n)
    if n % 2 == 0:
        n //= 2    # alternativt n = n // 2
    else:
        n = 3 * n + 1
print(n)


######################
# Tilleggsutfordring #
######################

maks_startverdi           = 10000
startverdi                = 2
startverdi_lengst_sekvens = 0
lengst_sekvens            = 0

while startverdi <= maks_startverdi:
    sekvenslengde = 0
    n = startverdi
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sekvenslengde += 1
    if sekvenslengde > lengst_sekvens:
        lengst_sekvens = sekvenslengde
        startverdi_lengst_sekvens = startverdi
    startverdi += 1

print(f"Den lengste sekvensen er på {lengst_sekvens} verdier, som man får om man starter med n = {startverdi_lengst_sekvens}")
