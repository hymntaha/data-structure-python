###### O(N) time complexity, O(N) space complexity

def two_sum(arr, target):
    ht = dict()
    for i in range(len(arr)):
        if arr[i] in ht:
            print(ht[arr[i]], arr[i])
            return True
        else:
            ht[target-arr[i]] = arr[i]

    return False


###### O(N) Time complexity and O(1) space
def two_sum_two_pointer(arr, target):
    i = 0
    j = len(arr) - 1

    while(i<j):
        if arr[i] + arr[j] == target:
            return arr[i],arr[j],
        elif arr[i] + arr[j] < target:
            i += 1
        else:
            j += 1
    return False

print(two_sum_two_pointer([-2,1,2,4,7,11], 13))
