def reverseWords(s):
    rev_sent = ""
    rev_str = ''
    for i in range(0,len(s)):
        if s[i] == ' ':
            rev_sent = rev_sent + rev_str + " "
            rev_str = ''
        else:
            rev_str = s[i] + rev_str

    return rev_sent + rev_str




print(reverseWords('Never say never'))
