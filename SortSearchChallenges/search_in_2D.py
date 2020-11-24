def find_in(lst, number):
    result = False

    for arr in lst:
        if number in arr:
            result = True

    return result



matrix  =[[10, 11, 12, 13],
           [14, 15, 16, 17],
           [27, 29, 30, 31],
           [32, 33, 39, 50]]

number = 99
print(find_in(matrix, number))
