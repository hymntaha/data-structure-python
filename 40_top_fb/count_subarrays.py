def count_subarrays(arr):
    # Write your code here
    left, right = [], []
    n = len(arr)
    res = [1] * n

    stack = []
    for i in range(n-1, -1, -1):
        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()
        if not stack:
            res[i] += n - 1 - i
        else:
            res[i] += stack[-1] - 1 - i
        stack.append(i)

    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()
        if not stack:
            res[i] += i
        else:
            res[i] += i - 1 - stack[-1]
        stack.append(i)
    return res

arr = [3, 4, 1, 6, 2]
print(count_subarrays(arr))
