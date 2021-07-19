def removeAdjacentDuplicates(str):
    output = []
    for ch in s:
        if output and ch == output[-1]:
            output.pop()
        else:
            output.append(ch)

    return ''.join(output)

s = "azxxzy"
print(removeAdjacentDuplicates(s))
