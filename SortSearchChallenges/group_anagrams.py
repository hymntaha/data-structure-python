def anagrams(lst):
    pairs = {}

    # Traversing all the lst strings
    for str in lst:

        # sorting the lst str and storing it in a key
        key = ''.join(sorted(str))

        # If the key is already in the dict then appending the original lst(Anagram)
        if key in pairs.keys():
            pairs[key].append(str)

        # if there is no key in the dict
        else:
            pairs[key] = []
            pairs[key].append(str)

    result = []

    # Traversing the whole dict and concat values and keys
    for key, value in pairs.items():
        if len(value) >= 2:
            result.append(value)

    result = sorted(result) # sort the list
    return result



input = [
    'tom marvolo riddle ',
    'abc',
    'def',
    'cab',
    'fed',
    'brag',
    'clint eastwood ',
    'i am lord voldemort',
    'elvis',
    'grab',
    'old west action',
    'lives'
]

print(anagrams(input))

"""
Time complexity is O(klogk) time in avg case using quick sort (where k is the length of the longest word in the given list)
so sorting n words would take O(n x klogk). 
"""
