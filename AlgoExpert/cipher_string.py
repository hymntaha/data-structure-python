def caesarCipherEncryptor(string, key):
    newLetters = []
    newKey = key % 26
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for letter in string:
        newLetters.append(getNewLetter(letter,newKey,alphabet))
    return "".join(newLetters)

def getNewLetter(letter,key,alphabet):
    newLetterCode = alphabet.index(letter) + key
    return alphabet[newLetterCode % 26]

key = 7
string = "mvklahvjcnbwqvtutmfafkwiuagjkzmzwgf" # Expected: tcrshocqjuidxcabatmhmrdpbhnqrgtgdnm
print(caesarCipherEncryptor(string,key))

"""
{
  "key": 15,
  "string": "kjwmntauvjjnmsagwgawkagfuaugjhawgnawgjhawjgawbfawghesh"
}
"""
