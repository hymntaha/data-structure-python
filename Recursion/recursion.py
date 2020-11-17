def find_uppercase_iterative(input_str):
    for i in range(len(input_str)):
        if input_str[i].isupper():
            return input_str[i]
    return "No uppercase character found"

def find_uppercase_recursive(input_str, idx=0):
    if input_str[idx].isupper():
        return input_str[idx]
    if idx == len(input_str) - 1:
        return "No uppercase character found"
    return find_uppercase_recursive(input_str, idx+1)

# input_str_1 = "lucidProgramming"
# input_str_2 = "LucidProgramming"
# input_str_3 = "lucidprogramming"
#
# print(find_uppercase_iterative(input_str_1))
# print(find_uppercase_iterative(input_str_2))
# print(find_uppercase_iterative(input_str_3))
#
# print(find_uppercase_recursive(input_str_1))
# print(find_uppercase_recursive(input_str_2))
# print(find_uppercase_recursive(input_str_3))

def print_len(str):
    if str == '':
        return 0
    print(print_len(str[1:]))
    return 1 + print_len(str[1:])

print(print_len('tacotuesday'))
