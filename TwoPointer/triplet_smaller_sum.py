def triplet_with_smaller_sum(arr, target):
    arr.sort()
    count = 0

    for i in range(len(arr) - 2):
        start = i + 1
        end = len(arr) - 1

        while start < end:
            sum = arr[i] + arr[start] + arr[end]

            if sum < target:
                count = count + end - start
                start += 1
            else:
                end -= 1

    return count

print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))


"""
Sorting array will take O(N * logN). Iterating twice will take O(N^2). 
So time complexity will be O(N*logN + N ^ 2) which is asymptotically O(N ^ 2)
Space complexity will take O(N)
"""
