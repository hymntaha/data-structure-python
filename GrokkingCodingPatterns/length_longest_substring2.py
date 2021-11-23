def lengthSubstring(str):
    charset = set()
    res = 0
    l = 0
    for r in range(len(str)):
        while str[r] in charset:
            charset.remove(str[l])
            l += 1
        charset.add(str[r])
        res = max(res, r - l + 1)
    return res
'''
Time complexity: O(N)
Space complexity: O(K) -> K = the number of distinct chars in the input str
'''

print(lengthSubstring("abcabcbb"))
