from stack import Stack

def reverse_string(str):
    s = Stack()
    reversed = ''
    for letter in str:
        s.push(letter)

    for i in str:
        reversed += s.pop()

    return reversed


print(reverse_string("!evitacudE ot emocleW"))
