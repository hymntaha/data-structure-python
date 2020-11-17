vowels = "aeiou"

def iterative_count(str):
    consonant_count = 0
    for i in range(len(str)):
        if str[i].lower() not in vowels and str[i].isalpha():
            consonant_count += 1

    return consonant_count


# print(iterative_count('tacotuesday'))

def recursive_count(str):
    if str == '':
        return 0

    if str[0].lower() not in vowels and str[0].isalpha():
        return 1+recursive_count(str[1:])
    else:
        return recursive_count(str[1:])

print(recursive_count('tacotuesday'))
