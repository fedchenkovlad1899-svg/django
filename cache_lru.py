from functools import lru_cache

@lru_cache
def positiv_sum(lst):
    if not lst:
        return 0
    if lst[0] > 0:
        return lst[0] + positiv_sum(lst[1:])
    else:
        return positiv_sum(lst[1:])

my_lst = [10, -2, 0, 5]

print(positiv_sum(tuple(my_lst)))