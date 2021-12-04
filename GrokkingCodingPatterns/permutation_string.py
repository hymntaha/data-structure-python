from collections import Counter

def permutiation_string(s1, s2):
    window = len(s1)
    s1_c = Counter(s1)

    for i in range(len(s2) - window+1):
        s2_c = Counter(s2[i:i+window])
        if s2_c == s1_c:
            return True

    return False



print('Permutation exist: ' + str(permutiation_string("abc","oidbcaf")))
print('Permutation exist: ' + str(permutiation_string("dc", "odicf")))
print('Permutation exist: ' + str(permutiation_string("bcdyabcdx","bcdxabcdy")))
print('Permutation exist: ' + str(permutiation_string("abc", "aaacb")))
