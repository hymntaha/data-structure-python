def longestSubstring(str, k):
    window_start = 0
    freqHash = {}
    max_length = 0

    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char not in freqHash:
            freqHash[right_char] = 0
        freqHash[right_char] += 1

        while len(freqHash) > k:
            left_char = str[window_start]
            freqHash[left_char] -= 1
            if freqHash[left_char] == 0:
                del freqHash[left_char]
            window_start += 1

        max_length = max(max_length, window_end-window_start+1)
    return max_length

str = 'cbbebi'
k = 3
print(longestSubstring(str, k))
