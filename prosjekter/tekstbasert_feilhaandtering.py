# -*- coding: utf-8 -*-
"""
Dette programmet går gjennom et enkelt lite tekstbasert spill, som til
tross for sin manglende lengde inneholder spenningsmomenter og skuffelser.

Dette er i tillegg ment som en forbedring til favoritten "tekstbasert_intro.py", da 
brukeren nå får mulighet til også å gjøre feil.

Laget av Tarjei
8. januar
"""

tekst = "Du våkner klokken 5:32 og føler deg våken, men vurderer å forsøke å fortsette å sove. Du ..."

valg_a = "står opp"
tekst_a = "... står opp og ser en gammel bok i bokhylla. Du ..."

valg_aa = "leser"
tekst_aa = "... får en fin start på dagen med en spennende bok."
valg_ab = "lar være"
tekst_ab = "... kjenner på en tomhetsfølelse som følger deg gjennom dagen."

valg_b = "sover videre"
tekst_b = "... sover og drømmer om et liv hvor muligheter gripes."

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
    

print(tekst)
valg = be_om_input(valg_a, valg_b)

if valg == valg_a:
    print(tekst_a)
    valg = be_om_input(valg_aa, valg_ab)
    if valg == valg_aa:
        print(tekst_aa)
    elif valg == valg_ab:
        print(tekst_ab)
    else:
        print(error)

elif valg == valg_b:
    print(tekst_b)
else:
    print(error)
