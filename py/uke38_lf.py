a = 22 # int(input(" >>> Tall #1: "))    
b = 7 # int(input(" >>> Tall #2: "))

# Vi skal lage et program som regner ut a * b
# Dette er et produkt

produkt = 0
i = 0     # tellevariabelen vår

while i <= b:          # Vi slutter når tellevariabelen er like stor som 'b'
    produkt += a
    i += 1

print(f"{a} ganger {b} = {produkt}")

kvotient = 0
divisor = a
dividend = b
while divisor >= dividend:
    kvotient = kvotient + 1        # kvotient += 1
    divisor = divisor - dividend   # divisor -= dividend

print(f"{a} delt på {b} er {kvotient}")
