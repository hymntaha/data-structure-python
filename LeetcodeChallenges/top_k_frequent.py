def topKFrequent(words, k):
    dict = {}
    for x in words:
        if x in dict:
            dict[x] += 1
        else:
            dict[x] = 1
    res = sorted(dict, key=lambda x: (-dict[x], x))
    return res[:k]


input = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
print(topKFrequent(input,k))


# This is O(NlogN)
