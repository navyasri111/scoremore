def self_power(n):
    return n**n
def sum_selfpowers(n):
    return str(sum(self_power(i) for i in range (1,n+1)))
print(sum_selfpowers(1000)[-10:])