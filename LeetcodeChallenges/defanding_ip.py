def defangIPaddr(str):
    result = ''
    for i in str:
        if i == '.':
            result += '[.]'
        else:
            result += i

    return result


address = "1.1.1.1"
print(defangIPaddr(address))
