def find_single_number(arr):
    num = 0
    for i in arr:
        num = num ^ i

    return num


arr = [1, 4, 2, 1, 3, 2, 3]
print(find_single_number(arr))

"""
001 - 1
010 - 2
011 - 3
100 - 4
101 - 5
110 - 6
111 - 7
"""
