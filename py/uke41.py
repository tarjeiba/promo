"""Introduksjon til funksjoner"""

def addisjon(tall1, tall2):
    """Returner summen av 'tall1' og 'tall2'."""
    return tall1 + tall2

summen = addisjon(15, 27)

print(f"Summen av {15} og {27} er {summen}.")

def stoerre_enn(tall1, tall2):
    """Returnerer hvorvidt tall1 er større enn tall2."""
    if tall1 > tall2:
        print(f"{tall1} er større enn {tall2}")
        return True
    else:
        print(f"{tall1} er ikke større enn {tall2}")
        return False

def er_partall(n):
    """Returner hvorvidt n er et partall.

    er_partall(4) #=> True
    er_partall(3) #=> False
    """
    svar = False      # for sikkerhets skyld
    if n % 2 == 0:    # n er et partall, dersom resten etter å dele på 2 er 0.
        print(f"{n} er et partall.")
        svar = True
    else:
        print(f"{n} er ikke et partall.")
        svar = False
    return svar       # Funksjonen er ferdig så fort den når return
        
def f(x):
    """Skriver ut 3x + 2."""
    svar = 3 * x + 2
    print(svar)
    return svar



############################
# VIKTIGST FRA DENNE TIMEN #
############################

# Vi lager en funksjon ved å bruke def
# ... dette kalles å definere en funksjon
def trippel(n):
    """Returner det triple av tallet 'n'."""
    # n  er en lokal variabel til trippel
    svar = 3 * n
    return svar

def hils():
    """Return en hyggelig hilsen."""
    return "Hei, godt å se deg."

# Vi bruker funksjonen ved å skrive
# funksjonsnavnet med parantes etter,
# og eventuelle parameter i parantesen

lite_tall = trippel(3)
stort_tall = trippel(trippel(trippel(123123123)))

print(lite_tall)
print(stort_tall)
