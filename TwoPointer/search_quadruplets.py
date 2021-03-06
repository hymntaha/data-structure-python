def search_quadruplets(arr, target):
    arr.sort()
    quadruplets = []

    for i in range(0, len(arr)-3):
        # skip same element to avoid duplicate quadruplets
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        for j in range(i + 1, len(arr)-2):
            # skip same element to avoid duplicate quadruplets
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue
            left = j + 1
            right = len(arr) - 1
            while (left < right):
                quad_sum = arr[i] + arr[j] + arr[left] + arr[right]
                if quad_sum == target:  # found the quadruplet
                    quadruplets.append(
                        [arr[i], arr[j], arr[left], arr[right]])
                    left += 1
                    right -= 1
                    while (left < right and arr[left] == arr[left - 1]):
                        left += 1  # skip same element to avoid duplicate quadruplets
                    while (left < right and arr[right] == arr[right + 1]):
                        right -= 1  # skip same element to avoid duplicate quadruplets
                elif quad_sum < target:
                    left += 1  # we need a pair with a bigger sum
                else:
                    right -= 1  # we need a pair with a smaller sum
    return quadruplets





arr = [4, 1, 2, -1, 1, -3]
target=1
print(search_quadruplets(arr, target))

"""
Time complexity: Sorting -> O(N*logN) and iteration will take O(N ^ 3). It is O(N * logN + N ^ 3) but asymptotically it will be O(N ^ 3)
Space complexity: O(N ^ 3)

"""
