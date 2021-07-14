import functools
import string

def int_to_string(x):
    is_negative = False
    if x<0:
        x, is_negative = -x, True

    s = []
    while True:
        print(ord('0'))
        print(chr(ord('0')))
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break

    return ('-' if is_negative else '') + ''.join(reversed(s))

def string_to_int(s):
    return functools.reduce(
        lambda running_sum, c: running_sum * 10 + string.digits.index(c),
        s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)

x = 432
print(int_to_string(x))
