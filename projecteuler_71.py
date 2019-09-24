import math
from fractions import Fraction

def is_properfraction(n):
    return [Fraction(i,n) for i in range(1,n) if math.gcd(i,n) == 1]
    
def is_sorted(n):
    fractionsInRange=[]
    for i in range(2,n+1):
        fractionsInRange.extend(is_properfraction(i))
    return sorted(fractionsInRange)

def is_previous_fraction(n):
    sortedFractions = is_sorted(n)
    return sortedFractions[sortedFractions.index(Fraction(3,7))-1]

print(is_previous_fraction(1000))