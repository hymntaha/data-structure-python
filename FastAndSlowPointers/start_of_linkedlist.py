from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()


def find_cycle_start(head):
    cycle_length = 0
    # find the linkedlist cycle

    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow== fast: # found the cycle
            cycle_length = calculate_ccyle_length(slow)
            break
    return find_start(head, cycle_length)

def calculate_ccyle_length(slow):
    current = slow
    cycle_length = 0
    while True:
        current = current.next
        cycle_length += 1
        if current == slow:
            break
    return cycle_length
def find_start(head, cycle_length):
    pointer1= head
    pointer2= head

    # move pointer2 ahead 'cycle_length' nodes
    while cycle_length > 0:
        pointer2 = pointer2.next
        cycle_length -= 1

    #increment both pointers until they meet at the start of the cycle
    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()

"""
Time complexity: O(N)
Space complexity: O(1)
"""
