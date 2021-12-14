def runLengthEncoding(string):
    encodedStringChar = []
    currentLength = 1

    for i in range(1,len(string)):
        currentChar = string[i]
        prevChar = string[i-1]

        if currentChar != prevChar or currentLength == 9:
            encodedStringChar.append(str(currentLength))
            encodedStringChar.append(prevChar)
            currentLength = 0
        currentLength += 1

    encodedStringChar.append(str(currentLength))
    encodedStringChar.append(string[len(string) - 1])

    return "".join(encodedStringChar)

string = "AAAAAAAAAAAAABBCCCCDD"
print(runLengthEncoding(string))
