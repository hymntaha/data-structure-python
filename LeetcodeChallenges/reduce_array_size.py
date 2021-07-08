def minSetSize(arr):
    # Sort the input numbers.
    arr.sort()

    # Generate the counts array.
    counts = []
    current_run = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            current_run += 1
            continue
        counts.append(current_run)
        current_run = 1
    counts.append(current_run)

    # Reverse sort the counts.
    counts.sort(reverse=True)

    # Remove numbers until at least half are removed.
    numbers_removed_from_arr = 0
    set_size = 0
    for count in counts:
        numbers_removed_from_arr += count
        set_size += 1
        if (numbers_removed_from_arr >= len(arr) // 2):
            break

    return set_size


nums = [3,3,3,3,5,5,5,2,2,7]
print(minSetSize(nums))

"""
size = 10


"""
