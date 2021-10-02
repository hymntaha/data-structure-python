def mergeTwoSortedList(lst1,lst2):
    x = 0
    y = 0
    m = 0
    result = []

    for i in range(len(lst1) + len(lst2)):
        result.append(i)

    while x < len(lst1) and y < len(lst1):
        if lst1[x] <= lst2[y]:
            result[m] = lst1[x]
            x += 1
            m += 1
        else:
            result[m] = lst2[y]
            y += 1
            m += 1

    while x < len(lst1):
        result[m] = lst1[x]
        x += 1
        m += 1
    while y < len(lst1):
        result[m] = lst2[y]
        y += 1
        m += 1
    return result
print(mergeTwoSortedList([1, 3, 4, 5],[2, 6, 7, 8]))
