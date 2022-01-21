def find_max_sum_nonadjacent(a):
    if len(a) < 1:
        return 0
    elif(len(a) == 1):
        return a[0]

    lengthA = len(a)
    result = []
    result.append(a[0])

    for i in range(1, lengthA):
        result.append(max(a[i], result[i - 1]))
        if i - 2 >= 0 :
            result[i] = max(result[i], a[i] + result[i - 2])

    return result[lengthA - 1]

v = [1,6,10, 14, -5,-1, 2, -1, 3]
sum = find_max_sum_nonadjacent(v)
print("Max sum of nonadjacent subsequence: " + str(sum))
