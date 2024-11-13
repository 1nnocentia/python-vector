#vector unit
import math
def unit_vector(v):
    #panjang = magnitudo
    panjang = math.sqrt(sum([i**2 for i in v]))
    unit_vector = [i/panjang for i in v]
    unit_vector = [round(i,2) for i in unit_vector]
    return unit_vector