import math

lessThan20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
thousands = ["","Thousand","Million","Billion"]

def numberToWords(num):
    if num == 0:
        return "Zero"
    res = ""
    for i in range(len(thousands)):
        if num % 1000 != 0:
            res = helper(num%1000) + thousands[i] + " " + res
        num /= 1000
    return res.strip()

def helper(num):
    if num == 0:
        return ""
    elif num < 20:
        return lessThan20[math.floor(num)] + " "
    elif num < 100:
        return tens[math.floor(num/10)] + " " + helper(num%10)
    else:
        return lessThan20[math.floor(num/100)] + " Hundred " + helper(num%100)

num = 1 234 567 891
print(numberToWords(num))
