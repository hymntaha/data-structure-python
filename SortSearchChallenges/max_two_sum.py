from decimal import Decimal

def find_max_prod(lst):
    sorted_lst = sorted(lst)
    return  sorted_lst[-2], sorted_lst[-1]

lst = [1, 3, 5, 2, 6]
print(find_max_prod(lst))
