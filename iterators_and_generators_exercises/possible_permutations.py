from itertools import permutations

def possible_permutations(lst):
    perm_list = permutations(lst)
    for el in perm_list:
        yield list(el)

[print(n) for n in possible_permutations([1, 2, 3])]
