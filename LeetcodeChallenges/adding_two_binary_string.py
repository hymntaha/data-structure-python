def addBinary(a,b):
    return f"{int(a,2) + int(b,2):b}"

a = "1010"
b = "1011"
print(addBinary(a,b))

def addBinary2(a,b):
    carry = 0
    result = ''

    a = list(a)
    b = list(b)

    while a or b or carry:
        if a:
            carry += int(a.pop())
        if b:
            carry += int(b.pop())

        result += str(carry % 2)
        carry //=2

    return result[::-1]
