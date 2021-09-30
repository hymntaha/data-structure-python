def find_product(lst):
    left = 1
    result = []

    for elem in lst:
        result.append(left)
        left = left * elem

    right = 1
    for i in range(len(lst) - 1, -1, -1):
        result[i] = right * result[i]
        right = right * lst[i]

    return result

print(find_product([1,2,3,4]))
