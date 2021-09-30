def find_sum(lst,k):
    for i in lst:
        if k-i in lst:
            return [i,k-i]

    return False

# Linear scan takes O(N) and sorting O(nlogn). Overall O(nlogn).
def find_sum2(lst,k):
    lst.sort()
    index1 = 0
    index2 = len(lst) - 1
    result = []
    sum = 0

    while index1 != index2:
        sum = lst[index1] + lst[index2]
        if sum < k:
            index1 += 1
        elif sum > k:
            index2 -= 1
        else:
            result.append(lst[index1])
            result.append(lst[index2])
            return result
    return False

lst = [1,21,3,14,5,60,7,6]
k = 81
print(find_sum2(lst,k))
