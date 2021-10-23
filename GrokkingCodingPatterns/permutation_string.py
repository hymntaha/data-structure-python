def permutiation_string(str, pat):
    window_start, matched = 0,0
    char_freq = {}

    for chr in pat:
        if chr not in char_freq:
            char_freq[chr] = 0
        char_freq[chr] += 1

    for window_end in range(len(str)):
        right = str[window_end]
        if right in char_freq:
            char_freq[right] -= 1
            if char_freq[right] == 0:
                matched += 1

        if matched == len(char_freq):
            return True

        if window_end >= len(pat) - 1:
            left = str[window_start]
            window_start += 1
            if left in char_freq:
                if char_freq[left] == 0:
                    matched -= 1
                char_freq[left] += 1

    return False



print('Permutation exist: ' + str(permutiation_string("oidbcaf", "abc")))
print('Permutation exist: ' + str(permutiation_string("odicf", "dc")))
print('Permutation exist: ' + str(permutiation_string("bcdxabcdy", "bcdyabcdx")))
print('Permutation exist: ' + str(permutiation_string("aaacb", "abc")))
