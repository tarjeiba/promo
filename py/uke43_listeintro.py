import matplotlib.pyplot as plt

# lag en selvvalgt mattefunksjon
def f(x):
    return x ** 2 + 3 * x - 15

# Velkommen til lister
xverdier = [4, 5, 8, 10, 13, -8]

# legger til en ekstra verdi
xverdier.append(9)

# bytter ut en verdi
xverdier[4] = 14

handleliste = ['smør',
               'egg',
               'mel',
               'sukker',
               4.4]

for vare in handleliste:
    print(vare)


print("-------------")
print("Og nå med while-løkke.")

      
i = 0
while i < len(handleliste):
    print(handleliste[i])
    i += 1


# Oppgave:
# - legg til 'bakepulver'
# - bytt ut 4.4 med 'strøssel'
