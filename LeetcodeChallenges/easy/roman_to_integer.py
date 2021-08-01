def romanToInt(s):
    res, prev = 0, 0
    rom = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    for i in reversed(s):          # rev the s
        if rom[i] >= prev:
            res += rom[i]     # sum the value iff previous value same or more
        else:
            res -= rom[i]     # substract when value is like "IV" --> 5-1, "IX" --> 10 -1 etc
        prev = rom[i]
    return res

str = "MCMXCIV"
print(romanToInt(str))
