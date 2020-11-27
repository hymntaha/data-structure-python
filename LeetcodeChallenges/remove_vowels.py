def remove_vowels(S):
    # result_string = ''
    # for letter in str:
    #     if letter in 'aeoui':
    #         pass
    #     else:
    #         result_string += letter
    # return result_string

    # With faster look up because of hashset/hash table
    retval = []
    vowels = set('aeiou')
    for letter in S:
        if letter not in vowels:
            retval.append(letter)
    return ''.join(retval)



print(remove_vowels('leetcodeisacommunityforcoders'))
