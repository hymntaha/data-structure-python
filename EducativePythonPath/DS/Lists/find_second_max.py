def find_second_maximum(lst):
    max = float("-inf")
    second_max = float("-inf")

    for i in lst:
        if i > max:
            max = i

    for i in lst:
        if i != max and i > second_max:
            second_max = i
    return second_max

print(find_second_maximum([4,2,3,5,1]))
