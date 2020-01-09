# -*- coding: utf-8 -*-
"""
Dette programmet går gjennom et enkelt lite tekstbasert spill, som til
tross for sin manglende lengde inneholder spenningsmomenter og skuffelser.

Dette er ment som en forbedring til 'tekstbasert_feilhaandtering', da det nå
også er lagt med en neglebitende kamp.

Laget av Tarjei
8. januar
"""

import random as rnd

def avgjoer(vaapen1, vaapen2):
    """Tar inn to strenger, hver enten 'stein', 'saks', eller 'papir'.

    Returverdier er som følger:
    vaapen1 > vaapen2  => 1
    vaapen2 > vaapen1  => 2
    vaapen1 == vaapen2 => 0

    Rangeringen er
    'stein' > 'saks' > 'papir'
    og 'papir' > 'stein'

    """

    if vaapen1 == "stein":
        if vaapen2 == "stein":
            return 0
        elif vaapen2 == "saks":
            return 1
        elif vaapen2 == "papir":
            return 2
    elif vaapen1 == "saks":
        if vaapen2 == "stein":
            return 2
        elif vaapen2 == "saks":
            return 0
        elif vaapen2 == "papir":
            return 1
    elif vaapen1 == "papir":
        if vaapen2 == "stein":
            return 1
        elif vaapen2 == "saks":
            return 2
        elif vaapen2 == "papir":
            return 0
    else:
        print("Det skjedde noe feil i avgjørelsen.")
            
def spill_steinsakspapir():
    """En funksjon du kan spille stein-saks-papir mot. Den returner følgende:
    spill_steinsakspapir() => 1 # spilleren vant
    spill_steinsakspapir() => 2 # funksjonen vant
    
    Funksjonen fortsetter å spille til det er kåret en vinner.

    Rangeringen av 'stein', 'saks', og 'papir' gjøres i 'avgjoer'-funksjonen.
    """

    vaapen = ["stein", "saks", "papir"]
    while True:
        spillers_valg = input(f" '{vaapen[0]}' / '{vaapen[1]}' / '{vaapen[2]}' ")
        spillers_valg = spillers_valg.lower().strip()
        mitt_valg = rnd.choice(vaapen)
        avgjoerelse = avgjoer(spillers_valg, mitt_valg)
        if avgjoerelse == 0:
            print("Uavgjort, vi prøver igjen...")
        elif avgjoerelse == 1:
            print("Æsj, du vant.")
            return 1
        elif avgjoerelse == 2:
            print("Ha ha, jeg vant!")
            return 2
        else:
            print("Vi klarte visst ikke helt dette, du og jeg.")

tekst = "Du våkner klokken 5:32 og føler deg våken, men vurderer å forsøke å fortsette å sove. Du ..."

valg_a = "står opp"
tekst_a = "... står opp og ser en gammel bok i bokhylla. Du ..."

valg_aa = "leser"
tekst_aa = """"... får en fin start på dagen med en spennende bok.

Med ett spretter det en gnom ut av boka og sier "Hei, jeg vil spille stein-saks-papir." Du  ..."""
valg_aaa = "godtar"
tekst_aaa = "Du gjør deg klar til kamp, tar fram nevene og velger..."
tekst_aaa1 = "Du vant kampen, for en lykke, for en glede, for en rus!"
tekst_aaa2 = "Du tapte kampen, mørket senker seg over sinnet ditt."

valg_aab = "avslår"
tekst_aab= "Du lukker boka, gnomen forsvinner, du fortsetter forundret med dagen din."

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
        valg = be_om_input(valg_aaa, valg_aab)
        if valg == valg_aaa:
            print(tekst_aaa)
            resultat = spill_steinsakspapir()
            if resultat == 1:
                print(tekst_aaa1)
            elif resultat == 2:
                print(tekst_aaa2)
        elif valg == valg_aab:
            print(tekst_aab)
    elif valg == valg_ab:
        print(tekst_ab)
elif valg == valg_b:
    print(tekst_b)
else:
    print(error)
