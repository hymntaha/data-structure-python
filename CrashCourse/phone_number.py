from typing import List
def letter_combinations_of_phone_number(digits):
    def dfs(path,res):
        if len(path) == len(digits):
            res.append(''.join(path))
            return

        next_number = digits[len(path)]
        for letter in KEYBOARD[next_number]:
            path.append(letter)
            dfs(path, res)
            path.pop()


    res = []
    dfs([], res)
    return res

KEYBOARD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}
inputs = ["56", "23", "235"]
for i in range(len(inputs)):
    print("Letter combinations of a phone number :",sorted(letter_combinations_of_phone_number(inputs[i])))

# Time comp: O(2^N)
