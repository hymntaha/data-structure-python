def validatePalindrome(s):
    def isPalindrome(str,l,r):
        while(l<=r):
            if str[l] != str[r]:
                return False
            else:
                l+=1
                r-=1
        return True

    n = len(s)
    indexA = 0
    indexB = n - 1

    while indexA <= indexB:
        if s[indexA] == s[indexB]:
            indexA += 1
            indexB -= 1
        else:
            if isPalindrome(s,indexA+1,indexB):
                return True
            elif isPalindrome(s, indexA, indexB-1):
                return True
            else:
                return False
        return True

str = 'abcad'
print(validatePalindrome(str))
