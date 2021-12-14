def generateDocument(chars, docs):
    freq_char = {}

    for i in chars:
        if i not in freq_char:
            freq_char[i] = 0
        freq_char[i] += 1

    for j in docs:
        if j not in freq_char or freq_char[j] == 0:
            return False
        freq_char[j] -= 1

    return True

'''
Time complexity: O(m+n) 
Space complexity: O(c) -> Number of unique characters
'''
chars = "Bste!hetsi ogEAxpelrt x "
docs = "AlgoExpert is the Best!"

print(generateDocument(chars,docs))
