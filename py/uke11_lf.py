#############
# Oppgave 0 #
#############

def prod_gt_n(a, b, n):
    return abs(a*b) > n
    
assert prod_gt_n(2, -3, 5) == True
assert prod_gt_n(1, 1, 2) == False
assert prod_gt_n(1, 2, 2) == False
assert prod_gt_n(3, 2, 2) == True
assert prod_gt_n(-1, -1, -1) == True
assert prod_gt_n(5, 5, 24) == True
assert prod_gt_n(3, -3, 8) == True
assert prod_gt_n(3, 3, 10) == False
print("Alle tester bestått.")

#############
# Oppgave 1 #
#############

def f(x):
    if x % 2 == 0:
        return True
    else:
        return False

# Hva gjør funksjonen f?
# - f returner True dersom x er et partall
# - ... den returner False dersom x ikke er et partall

def f(x):
    return x % 2 == 0

# Ja, det har Ivar helt rett i.

#############
# Oppgave 3 #
#############
# a
posisjonsfil = open("posisjonsmaalinger_til_test.txt", "r", encoding="utf-8-sig")
filtekst = posisjonsfil.read().splitlines()
posisjonsfil.close()

tider = []
posisjoner = []

for linje in filtekst:
    tid, posisjon = linje.split(";")
    tider.append(float(tid))
    posisjoner.append(float(posisjon))

# b
def delta(innliste):
    utliste = []
    i = 0
    while i < len(innliste) - 1:    # Trekker fra 1 for å unngå IndexError
        utliste.append(innliste[i+1] - innliste[i])
        i += 1
    return utliste

assert delta([5, 7, 8, -2, 0]) == [2, 1, -10, 2]
print("delta-test bestått.")


# c
delta_tider = delta(tider)
delta_posisjoner = delta(posisjoner)

# d
hastigheter = []

for delta_tid, delta_posisjon in zip(delta_tider, delta_posisjoner):
    hastighet = delta_posisjon / delta_tid
    hastigheter.append(hastighet)

# e
total_posisjonsendring = posisjoner[-1] - posisjoner[0]
total_tidsendring      = tider[-1]      - tider[0]

gjennomsnittsfart = total_posisjonsendring / total_tidsendring

# Gjennomsnittsfarten over målingene er altså -0.67 m/s
