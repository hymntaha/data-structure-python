def find_sum(lst,k):
    for i in lst:
        if k-i in lst:
            return [i,k-i]

    return False

lst = [1,21,3,14,5,60,7,6]
k = 81
print(find_sum(lst,k))
