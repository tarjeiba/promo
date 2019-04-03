import pygame
import random
import math

bakgrunnsfarge = (236, 240, 241)
bredde, hoyde = (800, 600)


def vektorsum(vector1, vector2):
    """Legg sammen to vektorer, vektor1 og vektor 2, hver en tuppel med vinkel og lengde.
    """
    vinkel1, lengde1 = vector1
    vinkel2, lengde2 = vector2

    x  = math.sin(vinkel1) * lengde1 + math.sin(vinkel2) * lengde2
    y  = math.cos(vinkel1) * lengde1 + math.cos(vinkel2) * lengde2
    
    vinkel = 0.5 * math.pi - math.atan2(y, x)
    lengde  = math.hypot(x, y)

    return (vinkel, lengde)

def finn_partikkel(partikkels, x, y):
    """Returner partikkel i posisjon (x, y), dersom ingen, returner None,

    Brukes om man velger en partikkel med musepekeren.
    """

    for p in partikkels:
        if math.hypot(p.x-x, p.y-y) <= p.strlse:
            return p
    return None

def kollider(p1, p2):
    """Kollider to partikler og endre deres fart og retning."""
    
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    dist = math.hypot(dx, dy)

    if dist < p1.strlse + p2.strlse:
        tangent = math.atan2(dy, dx)
        vinkel = 0.5 * math.pi + tangent

        vinkel1 = 2*tangent - p1.vinkel
        vinkel2 = 2*tangent - p2.vinkel

        p1.vinkel = vinkel1 
        p2.vinkel = vinkel2

        # For å unngå at partiklene fester seg til hverandre
        p1.x += math.sin(vinkel)
        p1.y -= math.cos(vinkel)
        p2.x -= math.sin(vinkel)
        p2.y += math.cos(vinkel)

class Partikkel(object):
    """Partikkel-klasse."""
    def __init__(self, pos, strlse):
        self.x, self.y = pos
        self.strlse = strlse    # størrelse
        self.farge = (0, 0, 255)
        self.tykkelse = 0
        self.fart = 0
        self.vinkel = 0
        # oppgave a)

    def display(self):
        """Tegne partikkelen på skjermen."""
        pygame.draw.circle(screen, self.farge, (int(self.x), int(self.y)), self.strlse, self.tykkelse)

    def flytt(self):
        """Flytt the partikkel according to its velocity (fart and direction)."""
        self.x += math.sin(self.vinkel) * self.fart
        self.y -= math.cos(self.vinkel) * self.fart

    def sprett(self):
        """Sprett partikkel against walls ceiling, or floor."""
        if self.x > bredde - self.strlse:
            self.x = 2*(bredde - self.strlse) - self.x
            self.vinkel = - self.vinkel

        elif self.x < self.strlse:
            self.x = 2*self.strlse - self.x
            self.vinkel = - self.vinkel

        if self.y > hoyde - self.strlse:
            self.y = 2*(hoyde - self.strlse) - self.y
            self.vinkel = math.pi - self.vinkel

        elif self.y < self.strlse:
            self.y = 2*self.strlse - self.y
            self.vinkel = math.pi - self.vinkel


screen = pygame.display.set_mode((bredde, hoyde))
pygame.display.set_caption('Partikkel collisions')

number_of_partikkels = 2
mine_partikler = []

for n in range(number_of_partikkels):
    strlse = random.randint(10, 20)
    x = random.randint(strlse, bredde-strlse)
    y = random.randint(strlse, hoyde-strlse)

    partikkel = Partikkel((x, y), strlse)
    partikkel.fart = random.random()
    partikkel.vinkel = random.uniform(0, math.pi*2)

    mine_partikler.append(partikkel)

valgt_partikkel = None
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            valgt_partikkel = finn_partikkel(mine_partikler, mouseX, mouseY)
        elif event.type == pygame.MOUSEBUTTONUP:
            valgt_partikkel = None

    if valgt_partikkel:
        (mouseX, mouseY) = pygame.mouse.get_pos()
        dx = mouseX - valgt_partikkel.x
        dy = mouseY - valgt_partikkel.y
        valgt_partikkel.vinkel = 0.5*math.pi + math.atan2(dy, dx)
        valgt_partikkel.fart = math.hypot(dx, dy) * 0.1

    screen.fill(bakgrunnsfarge)

    for i, partikkel in enumerate(mine_partikler):
        partikkel.flytt()
        partikkel.sprett()
        for partikkel2 in mine_partikler[i+1:]:
            kollider(partikkel, partikkel2)
        partikkel.display()

    pygame.display.flip()

pygame.quit()
