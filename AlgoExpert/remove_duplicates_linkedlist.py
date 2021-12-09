class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    cur = linkedList
    while cur:
        while cur.next and cur.next.value == cur.value:
            cur.next = cur.next.next
        cur = cur.next

    return linkedList

def main():
    list = LinkedList(1)
    list.next = LinkedList(1)
    list.next.next = LinkedList(2)
    list.next.next.next = LinkedList(3)
    list.next.next.next.next = LinkedList(4)
    list.next.next.next.next.next = LinkedList(4)
    list.next.next.next.next.next.next = LinkedList(4)
    list.next.next.next.next.next.next.next = LinkedList(5)
    list.next.next.next.next.next.next.next.next = LinkedList(6)
    list.next.next.next.next.next.next.next.next.next = LinkedList(6)

    print(removeDuplicatesFromLinkedList(list))
