import collections
from collections import Counter

def are_they_equal(array_a, array_b):

    counter = collections.defaultdict(int)
    for t in array_b:
        counter[t] += 1
    for a in array_a:
        if a not in counter or counter[a] == 0:
            return False
        counter[a] -= 1
    return all(v == 0 for v in counter.values())

    # return Counter(array_a) == Counter(array_b)

a_1 = [1, 2, 3, 4]
b_1 = [1, 4, 3, 2]
print(are_they_equal(a_1, b_1))
# a_2 = [1, 2, 3, 4]
# b_2 = [1, 2, 3, 5]
# print(are_they_equal(a_2, b_2))
