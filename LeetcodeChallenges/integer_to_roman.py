'M': 1000,
'CM': 900,
'D': 500,
'CD': 400,
'C': 100,
'XC': 90,
'L': 50,
'XL': 40,
'X': 10,
'IX': 9,
'V': 5,
'IV': 4,
'I': 1
}

res = ''

while num:

    for i in values.keys():

        div = num // values[i]

        if div > 0:
            for j in range(div):
                res += i

            mod = num % values[i]
            num = mod

return res
