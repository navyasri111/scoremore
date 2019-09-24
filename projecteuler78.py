import itertools as it

def combinations(n,i):
    list_numbers = [i for i in range(1,n+1)]
    return list(it.combinations(list_numbers,i))
print(combinations(5,2))
# def all_combinations(n):
#     list = []
#     for i in range(2,n+1):
#         list += combinations(n,i)
#     return list
# print(all_combinations(5))
