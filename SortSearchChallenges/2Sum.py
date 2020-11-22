def two_sum(arr, tar):
    dic = {}
    for i, n in enumerate(arr):
        if n in dic:
            return [arr[dic[n]], n]
        dic[tar-n] = i


print(two_sum([1,21,3,14,5,60,7,6], 81))
