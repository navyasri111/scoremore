def is_prime(n):
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    if n % 2 == 0:
        return False
    r = 3
    while(r * r <= n ):
        if n % r == 0:
            return False
        r += 2
    return True

def is_square(n):
    for i in range(1,(n//2)+1):
        if n == i*i:
            return True
        
def goldbachs(n):
    primes = [i for i in range(2,n) if is_prime(i)]
    for prime in primes: 
        if is_square((n - prime) // 2) :
            return True
    return False

def is_goldbachs():
    for i in range(3,40,2):
        if not is_prime(i) and goldbachs(i):
            print(i)
is_goldbachs()