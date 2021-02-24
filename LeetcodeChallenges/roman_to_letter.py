values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def romanToInt(s: str) -> int:
    total = 0
    i = 0
    while i < len(s):
        # If this is the substractive case.
        if i + 1 < len(s) and values[s[i]] < values[s[i+1]]:
            total += values[s[i+1]] - values[s[i]]
            i += 2
        # Else this is NOT the substractive case.
        else:
            total += values[s[i]]
            i += 1
    return total

print(romanToInt('MMCMLXXXIX'))
"""
Time complexity : O(1).
As there is a finite set of roman numerals, the maximum number possible number can be 3999, which in roman numerals is MMMCMXCIX. As such the time complexity is O(1).
If roman numerals had an arbitrary number of symbols, then the time complexity would be proportional to the length of the input, i.e. O(n). This is assuming that looking up the value of each symbol is O(1).

Space complexity : O(1).
Because only a constant number of single-value variables are used, the space complexity is O(1).
"""
