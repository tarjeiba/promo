import math

def deg_til_rad(vinkel):
    """Tar inn vinkel i grader og oversetter til radianer."""
    
    rad = math.radians(vinkel)
    return rad

def sin_i_grader(vinkel):
    """Tar inn vinkel i grader og 
    returnerer sinus av vinkelen."""
    
    radden = deg_til_rad(vinkel)
    return math.sin(radden)
