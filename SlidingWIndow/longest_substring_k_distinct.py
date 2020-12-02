def longestSubstring(str, k):
    window_start =0
    max_length = 0
    char_freq = {}

    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char not in char_freq:
            char_freq[right_char] = 0
        char_freq[right_char] += 1

        if len(char_freq) > k:
            left_char = str[window_start]
            window_start += 1
            char_freq[left_char] -= 1
            if char_freq[left_char] == 0:
                del char_freq[left_char]

        max_length = max(max_length, window_end-window_start+1)

    return max_length

str = 'cbbebi'
k = 3
print(longestSubstring(str, k))
