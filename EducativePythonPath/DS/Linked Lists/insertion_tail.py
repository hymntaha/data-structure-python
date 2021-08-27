class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None

class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if(self.head_node is None):  # Check whether the head is None
            return True
        else:
            return False

    # Supplementary print function
    def print_list(self):
        if(self.is_empty()):
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True

def insert_at_tail(lst, value):
    # Creating a new node
    new_node = Node(value)

    # Check if the list is empty, if it is simply point head to new node
    if lst.get_head() is None:
        lst.head_node = new_node
        return

    # if list not empty, traverse the list to the last node
    temp = lst.get_head()

    while temp.next_element:
        temp = temp.next_element

    # Set the nextElement of the previous node to new node
    temp.next_element = new_node
    return

def search(lst, value):

    # Start from first element
    current_node = lst.get_head()

    # Traverse the list till you reach end
    while current_node:
        if current_node.data == value:
            return True  # value found
        current_node = current_node.next_element

    return False  # value not found

def delete(lst, value):
    deleted = False
    if lst.is_empty():  # Check if list is empty -> Return False
        print("List is Empty")
        return deleted
    current_node = lst.get_head()  # Get current node
    previous_node = None  # Get previous node
    if current_node.data == value:
        lst.delete_at_head()  # Use the previous function
        deleted = True
        return deleted

    # Traversing/Searching for Node to Delete
    while current_node is not None:
        # Node to delete is found
        if value == current_node.data:
            # previous node now points to next node
            previous_node.next_element = current_node.next_element
            current_node.next_element = None
            deleted = True
            break
        previous_node = current_node
        current_node = current_node.next_element

    if deleted == False:
        print(str(value) + " is not in list!")
    else:
        print(str(value) + " deleted!")

    return deleted

def length(lst):
    if lst.is_empty():
        return 0

    curr_node = lst.get_head()
    cnt = 1

    while curr_node.next_element:
        cnt += 1
        curr_node = curr_node.next_element

    return cnt

def detect_loop(lst):
    # Keep two iterators
    onestep = lst.get_head()
    twostep = lst.get_head()

    while onestep and twostep and twostep.next_element:
        onestep = onestep.next_element # moves one node at a time
        twostep = twostep.next_element.next_element # skips a node
        if onestep == twostep: # loop exists
            return True
    return False

def find_mid(lst):
    length = lst.length()

    mid = 0
    if length % 2 == 0:
        mid = length // 2
    else :
        mid = (length // 2) + 1

    curr = lst.get_head()
    count = 1
    middle_node = 0

    while curr:
        if count == mid:
            middle_node = curr.data
        curr = curr.next_element

    return middle_node

lst = LinkedList()
lst.insert_at_head(1)
lst.insert_at_head(4)
lst.insert_at_head(3)
lst.insert_at_head(2)
lst.print_list()
delete(lst, 4)
lst.print_list()
