def validate_parantheses(str):
    parantheses_hash = {')':'(',']':'[','}':'{'}
    stack = []

    for i in str:
        if i in parantheses_hash:
            if stack and stack[-1] == parantheses_hash[i]:
                stack.pop()
            else:
                return False

        else:
            stack.append(i)

    return True if not stack else False


# print(validate_parantheses("()"))
# print(validate_parantheses("()[]{}"))
print(validate_parantheses("({[]})"))



