# -*- coding: utf-8 -*-
"""
Dette programmet går gjennom et enkelt lite tekstbasert spill, som til
tross for sin manglende lengde inneholder spenningsmomenter og skuffelser.

Dette er i tillegg ment som en forbedring til favoritten "tekstbasert_intro.py", da 
brukeren nå får mulighet til også å gjøre feil.

Laget av Tarjei
8. januar
"""

tekst_1 = "Du våkner klokken 5:32 og føler deg våken, men vurderer å forsøke å fortsette å sove. Du ..."

valg_1a = "står opp"
tekst_1a = "... står opp og ser en gammel bok i bokhylla. Du ..."

valg_1aa = "leser"
tekst_1aa = "... får en fin start på dagen med en spennende bok."
valg_1ab = "lar være"
tekst_1ab = "... kjenner på en tomhetsfølelse som følger deg gjennom dagen."

valg_1b = "sover videre"
tekst_1b = "... sover og drømmer om et liv hvor muligheter gripes."

error = "Det var jommen et ugyldig valg, fysikkens lover er brutt."

def be_om_input(alt1, alt2):
    """Ber spilleren om å taste inn input til spillet, og gir seg først når
    spilleren har tastet inn noe gyldig.
    
    Returnerer valget brukeren tastet inn når dette er gyldig.

    Eksempel på bruk:
    valg = be_om_input('gå', 'løp')

    'gå' / 'løp' >>> går
    Ugyldig alternativ, prøv igjen.
    'gå' / 'løp' >>> gå     # valg er nå 'gå'
    """
    valgt = None
    while valgt != alt1 and valgt != alt2:
        valgt = input(f"'{alt1}' / '{alt2}'").lower().strip()
    return valgt
    

print(tekst_1)
valg = be_om_input(valg_1a, valg_1b)

if valg == valg_1a:
    print(tekst_1a)
    valg = be_om_input(valg_1aa, valg_1ab)
    if valg == valg_1aa:
        print(tekst_1aa)
    elif valg == valg_1ab:
        print(tekst_1ab)
    else:
        print(error)

elif valg == valg_1b:
    print(tekst_1b)
else:
    print(error)
