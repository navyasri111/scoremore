import math

def is_decimal_sum(n):
    return sum(map(int,str(math.sqrt(n) % 1)[2:103]))

def is_total_sum(n):
    return sum(is_decimal_sum(i) for i in range (0,n+1))
    
print(is_total_sum(100))