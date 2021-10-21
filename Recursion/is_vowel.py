def is_vowel(letter):
    letter = letter.lower()
    vowels = 'aeiou'

    if letter in vowels:
        return 1
    else:
        return 0

def count_vowels(string,n):
    if n == 1:
        return is_vowel(string[0])

    return count_vowels(string,n-1) + is_vowel(string[n-1])

str = 'Educative'
print(count_vowels(str, len(str)))
