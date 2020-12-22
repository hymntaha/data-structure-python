def backspace_compare(str1, str2):
    indexA, indexB = len(str1) - 1, len(str2) - 1
    count_A = count_B = 0

    while indexA >= 0 or indexB >= 0:
        # si stops at non-deleted character in str1 or -1
        while indexA >= 0:
            if str1[indexA] == '#':
                count_A += 1
                indexA -= 1
            elif str1[indexA] != '#' and count_A > 0:
                count_A -= 1
                indexA -= 1
            else:
                break

        # ti stops at non-deleted character in str2 or -1
        while indexB >= 0:
            if str2[indexB] == '#':
                count_B += 1
                indexB -= 1
            elif str2[indexB] != '#' and count_B > 0:
                count_B -= 1
                indexB -= 1
            else:
                break

        if ( indexA < 0 and indexB >= 0 ) or ( indexA < 0 and indexB >= 0 ):
            # eg. str1 = 'a#', str2 = 'a'
            return False

        if( indexA >= 0 and indexB >= 0 ) and str1[indexA] != str2[indexB]:
            return False

        indexA -= 1
        indexB -= 1
    return True

str1="xy#z"
str2="xzz#"

print(backspace_compare(str1, str2))

"""
Time complexity is O(M+N)
Space complexity is O(1)
"""
