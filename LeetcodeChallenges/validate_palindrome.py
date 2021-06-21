def validatePalindrome(s):
    def check(l,r,s):
        while l<=r:
            if s[l]!=s[r]:
                return False
            else:
                l+=1
                r-=1
        return True

    n = len(s)
    l=0
    r=n-1
    while l<=r:
        if s[l]==s[r]:
            l+=1
            r-=1
        else:
            if check(l+1, r, s):
                return True
            elif check(l,r-1,s):
                return True
            else:
                return False
    return True

str = 'abca'
print(validatePalindrome(str))
