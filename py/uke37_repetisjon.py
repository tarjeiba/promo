mitt_navn = "tarjei"

ditt_navn = input("Hva er navnet ditt? ")

lengde_mitt_navn = len(mitt_navn)
lengde_ditt_navn = len(ditt_navn)

if lengde_mitt_navn == lengde_ditt_navn: print("Hurra") elif lengde_mitt_navn > lengde_ditt_navn:
    print("oisann, litt for kort") else: print("det var jommen langt.")  # Gjør en test som skriver
    ut 'hurra' # om navnene er like lange

# ... 'oisann, litt for kort' om har et litt for kort navn

# ... 'altfor langt'

# Dere kommer til å trenge: - len() - if / elif / else
