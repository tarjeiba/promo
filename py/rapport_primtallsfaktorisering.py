#########################################################
# Et program som finner største primtallsfaktor i       #
# TALL. Brukt under løsning av Project Euler oppgave 3. #
#                                                       #
# Skrevet av Tarjei Bærland, 3. mars 2020.              #
#########################################################

import time

starttid = time.time()
TALL = tall = 600851475143
teller = 2

while teller < tall:
    while tall % teller == 0:
        tall //= teller
    teller += 1

sluttid = time.time()
print(f"Den største primtallsfaktoren i {TALL} er {tall}.")
print(f"Denne utregningen tok {sluttid-starttid:.4f} sekunder.")
