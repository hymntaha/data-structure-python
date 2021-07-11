def reverseWords(s):
    def reverse(i, j):
        while 0 <= i < j < len(s):
            s[i], s[j] = s[j], s[i]
            i, j = i + 1, j - 1

    s.append(" ")
    start = 0
    for i, v in enumerate(s):
        if v == " ":
            reverse(start, i - 1)
            start = i + 1
    s.pop()
    reverse(0, len(s) - 1)
    return s

str = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
print(reverseWords(str))
