from collections import Counter


def checkInclustion(s1,s2 ):
    window = len(s1)
    s1_c = Counter(s1)

    for i in range(len(s2)-window+1):
        s2_c = Counter(s2[i:i+window])
        if s2_c == s1_c:
            return True

    return False
    # dict1 = {} # the first dict keep track of count in s1
    # dict2 = {} # the second dict keep track of count for portion of s2
    # size = len(s1)
    # length = len(s2)
    #
    # for key in s1: # initiate two dicts, fill in 0s for dict2
    #     dict1[key] = dict1.get(key, 0) + 1
    #     dict2[key] = 0
    #
    # for c in s2[0:size]: #for the first size elements in s2, fill in
    #     if c in dict2:
    #         dict2[c] += 1
    # if dict2 == dict1: # check if dict1 == dict2
    #     return True
    #
    # for i in range(1, length - size + 1): # slide through s2 and update dict2
    #     cur = s2[i-1]
    #     new = s2[i+size-1]
    #     if cur in dict2:
    #         dict2[cur] -= 1
    #     if new in dict2:
    #         dict2[new] += 1
    #     if dict2 == dict1: # check if dict1 == dict2
    #         return True
    # return False

s2 = 'ba'
str2 = 'eidboaoo '
print(checkInclustion(s2,str2))
