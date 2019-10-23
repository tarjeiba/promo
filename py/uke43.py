import matplotlib.pyplot as plt

# lag en selvvalgt mattefunksjon
def f(x):
    return x ** 2 + 3 * x - 15

# Ønsker å lage en liste med alle tallene fra 0 til 10

xverdier = list( range(0, 11))
print(xverdier)

yverdier = [] # tom liste, som skal ha yverdiene

# Oppgave :
# gjør det så yverdier inneholder f(x) for alle verdiene
# i xverdier

for xverdi in xverdier:
    yverdi = f(xverdi)
    print(f"Er på x-verdi {xverdi}.")
    print(f"Legger {yverdi} til lista yverdier.")
    yverdier.append( yverdi )

# Vi har nå en liste med xverdier og en med yverdier
# og er klare til å plotte

fig, ax = plt.subplots()

graf1, = ax.plot(xverdier, yverdier)

fig.savefig('mitt_foeste_plot.png')
fig.show()
