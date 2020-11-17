from stack import Stack

def convert(dec):
    s = Stack();

    while (dec >= 1):
        left = dec % 2
        s.push(left)
        dec = dec // 2

    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num

print(convert(242))
