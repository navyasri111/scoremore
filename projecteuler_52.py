def is_same(n):
    t = sorted(str(n))
    if t == sorted(str(n*2)) and t == sorted(str(n*3)) and t == sorted(str(n*4)) and t == sorted(str(n*5)) and t == sorted(str(n*6)):
        return True
    return False
def permuted_multiples():
    for i in range(10000,1000000):
        if is_same(i):
            return i
print(permuted_multiples())