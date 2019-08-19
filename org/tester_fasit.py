posisjonsfil = open("posisjonsmaalinger_til_test.txt", "r", encoding="utf-8-sig")
filtekst = posisjonsfil.read().splitlines()
posisjonsfil.close()

tider = []
posisjoner = []

for linje in filtekst:
    temp = linje.split(";")
    tider.append(float(temp[0]))
    posisjoner.append(float(temp[1]))

def delta(innliste):
    n = len(innliste) - 1
    utliste = [0] * n
    for i in range(n):
        utliste[i] = innliste[i+1] - innliste[i]
    return utliste

delta_posisjon = delta(posisjoner)
delta_tid = delta(tider)


print(f"Til fasit: sum(tider) == {sum(tider)}")
print(f"Til fasit: sum(posisjoner) == {sum(posisjoner)}")

print(f"Til fasit: sum(delta_posisjon) == {sum(delta_posisjon)}")
print(f"Til fasit: sum(delta_tid) == {sum(delta_tid)}")


hastigheter = []
for (dp, dt) in zip(delta_posisjon, delta_tid):
    hastigheter.append(dp/dt)

print(f"Til fasit: sum(hastigheter) == {sum(hastigheter)}")
