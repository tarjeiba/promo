# Be brukeren om et tall
tall = input("Skriv inn et tall:")
# Endre 'tall' til ikke å være tekststreng
tall = int(tall) # nå er det et heltall


print("Du ga meg tallet: ", tall)

if tall > 10:
    print("Oi. Det var stort!")
    print("Jeg er fortsatt i if-setninga.")
else:
    print("Jøsses ... det var et bitte lite tall.")
