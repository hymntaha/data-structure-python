def find_product(lst):
    prod = []
    left = 1
    for i in range(len(lst)):
        prod.append(left)
        left = left * lst[i]

    right = 1
    for i in range(len(lst) - 1, -1, -1):
        prod[i] = right * prod[i]
        right = right * lst[i]
    return prod

print(find_product([1,2,3,4]))
