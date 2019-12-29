"""
Oppgave:
- be brukeren om ett tall og to ord
- skriv ut til brukeren hvorvidt summen av vokalene i de to ordene er større enn tallet eller ikke.

Eksempel på bruk av programmet kan være som følger:

>>> Gi meg et tall, takk.
8
>>> Gi meg et ord, takk.
hei
>>> Gi meg et ord til, takk.
hvorfor

Summen av antall vokaler i ordene 'hei' og 'hvorfor' er 4, dette er mindre enn 8. Hadet!


Tips:
- Implementer noe enklere først, ta kun ett ord, tell kun en type vokal
- Du kan iterere over en tekststreng på samme måte som vi gjør i en liste, se under.
- Du kan sjekke om en bokstav er i et ord ved å bruke `in`, se under.

>>> for bokstav in "liten tekst":
...     print(bokstav)

l
i
t
e
n
 
t
e
k
s
t



>>> tekst = "liten tekst"
>>> if 'i' in tekst:
...     print("Bokstaven 'i' er i teksten.")

Bokstaven 'i' er i teksten.


Laget av Tarjei Bærland, 29. desember 2019.
"""

def er_vokal(c):
    """Returner hvorvidt 'c' er en vokal."""
    svar = c.lower() in "aeiouyæøå"
    return svar

# Del 1 -- Be om input og lagre dette
tall = int(input("Gi meg et tall, takk.\n"))
ord1 = input("Gi meg et ord, takk.\n")
ord2 = input("Gi meg et ord, takk.\n")

antall_vokaler = 0 # Initialiserer telleren

###############################
# Del 2 -- Gjør utregninger   #
###############################
for c in ord1 + ord2:
    if er_vokal(c):
        antall_vokaler += 1

# Del 3 -- Skriv ut resultater
if antall_vokaler < tall:
    komparator = "mindre enn"
elif antall_vokaler > tall:
    komparator = "større enn"
else:
    komparator = "like mye som"

print(f"Summen av antall vokaler i ordene '{ord1}' og '{ord2}' er \
{antall_vokaler}, dette er {komparator} {tall}. Hadet!")
