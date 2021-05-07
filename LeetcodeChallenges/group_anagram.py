from collections import defaultdict

def groupAnagrams(strs):
    count = defaultdict(list)

    for word in strs:
        key = ''.join(sorted(word))
        count[key].append(word)

    return list(count.values())

input = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(input))


"""Time complexity: O(n) Space complexity: O(n)"""
