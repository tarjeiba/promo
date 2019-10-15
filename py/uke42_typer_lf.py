"""Dette programmet lister opp typen til noen ulike verdier.

Laget av Tarjei
"""
def utregning(x):
    """Tar inn et tall x, og gjør litt matte."""
    dobbel_x = 2 * x
    litt_mindre = dobbel_x - 5
    return litt_mindre * dobbel_x

def er_stort(testtall, stort_tall):
    """Tar inn to tall og returnerer hvorvidt 'testtall'
    er større enn 'stort_tall'.
    """
    returverdi = False
    if testtall > stort_tall:
        returverdi = True
    return returverdi


# I alle linjene under, fyll ut det som står i anførselstegn
# når du skriver venstre side inn i konsollen.

# Eksempel:
# type(3.1) == 'float'
# siden
# >>> type(3.1)
# <class 'float'>

# Oppgaver:
# type(3) == 'int'
# type(2 + 2) == 'int'
# type(utregning(5)) == 'int'

svar = utregning(5)

# type(svar) == 'int'
# type(er_stort(3, 2)) == 'bool'
# type(er_stort(2, 3)) == 'bool'
# type(er_stort) == 'function'
