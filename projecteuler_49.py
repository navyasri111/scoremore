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

def is_prime_permutations(n):
    if is_prime(n):
        if is_prime(n+3330) and sorted(str(n+3330)) == sorted(str(n)) :
            if is_prime(n+6660) and sorted(str(n+6660)) == sorted(str(n)) :
                return True
    return False

def twelve_digit_num():
    for i in range(1488,10000):
        if is_prime_permutations(i):
            print((str(i) + str(i+3330) + str(i+6660)))
            break
twelve_digit_num()