# -*- coding: utf-8 -*-
"""
Dette programmet går gjennom et enkelt lite tekstbasert spill, som til
tross for sin manglende lengde inneholder spenningsmomenter og skuffelser.

Laget av Tarjei
8. januar
"""

print("Du våkner klokken 5:32 og føler deg våken, men vurderer å forsøke å fortsette å sove. Du ...")

valg = input("'står opp' / 'sover videre'")
error = "Det var jommen et ugyldig valg, fysikkens lover er brutt."

if valg == "står opp":
    print("... står opp og ser en gammel bok i bokhylla. Du ...")
    valg = input("'leser' / 'lar være'")
    if valg == "leser":
        print("... får en fin start på dagen med en spennende bok.")
    elif valg == "lar være":
        print("... kjenner på en tomhetsfølelse som følger deg gjennom dagen.")
    else:
        print(error)
elif valg =="sover videre":
    print("... sover og drømmer om et liv hvor muligheter gripes.")
else:
    print(error)
