def count_subarrays(arr):
    n = len(arr)
    res = [1] * n
    stack = [-1]
    #left
    for i in range(n):
        while len(stack) > 1 and arr[stack[-1]] < arr[i]:
            stack.pop()
        res[i] += i - stack[-1] - 1
        stack.append(i)

    # from right
    stack = [n]
    for i in range(n - 1, -1, -1):
        while len(stack) > 1 and arr[stack[-1]] < arr[i]:
            stack.pop()
        res[i] += stack[-1] - i - 1
        stack.append(i)
    return res
test_1 = [3, 4, 1, 6, 2]
print(count_subarrays(test_1))
'''
def count_subarrays(arr):
    output = [1] * len(arr)
    for i in range(len(arr)):
        k = i
        while k - 1 >= 0 and arr[k - 1] < arr[i]:
            output[i] += 1
            k -= 1
        
        k = i
        while k + 1 < len(arr) and arr[k + 1] < arr[i]:
            output[i] += 1
            k += 1
    return output

'''
