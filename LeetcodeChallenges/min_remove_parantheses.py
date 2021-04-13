def minRemoveToMakeValid(s):
    s = list(s)
    stack = []

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                s[i] = ''

    while stack:
        s[stack.pop] = ''
    return ''.join(s)


string = "lee(t(c)o)de)"
print(minRemoveToMakeValid(string))

# time complexity: O(n)
# space complexity: O(n)
