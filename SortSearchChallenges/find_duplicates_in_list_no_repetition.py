def find_duplicates(lst):
    result = []  # A list to store duplicates

    dict = {}

    for num in lst:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1

    for key, value in dict.items():
        if(value > 1):
            result.append(key)

    return result

lst = [1, 3, 1, 3, 5, 1, 4, 7, 7]
print(find_duplicates(lst))
# result = [1, 3, 7]


# Since the list is traversed only once and removing duplication also takes O(N) time, overall time complexity
# of this solution is O(N).

# TODO: Space complexity analysis
