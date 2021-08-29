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
    if lst.is_empty():
        return -1

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

def remove_duplicates(lst):
    if lst.is_empty():
        return None

    # If list only has one node, leave it unchanged
    if lst.get_head().next_element is None:
        return lst

    outer_node = lst.get_head()
    while outer_node:
        inner_node = outer_node  # Iterator for the inner loop
        while inner_node:
            if inner_node.next_element:
                if outer_node.data == inner_node.next_element.data:
                    # Duplicate found, so now removing it
                    new_next_element = inner_node.next_element.next_element
                    inner_node.next_element = new_next_element
                else:
                    # Otherwise simply iterate ahead
                    inner_node = inner_node.next_element
            else:
                # Otherwise simply iterate ahead
                inner_node = inner_node.next_element
        outer_node = outer_node.next_element

    return lst
def union(list1, list2):
    curr_node = list1.get_head()
    last_node = curr_node

    while curr_node.next_element:
        curr_node = curr_node.next_element
        last_node = curr_node

    lst_2_node = list2.get_head()

    last_node.next_element = lst_2_node

    while lst_2_node.next_element:
        last_node = lst_2_node
        lst_2_node = lst_2_node.next_element

    return list1

# Returns a list containing the intersection of list1 and list2


def intersection(list1, list2):

    result = LinkedList()
    visited_nodes = set()  # Keep track of all the visited nodes
    current_node = list1.get_head()

    # Traversing list1 and adding all unique nodes into the hash set
    while current_node:
        value = current_node.data
        if value not in visited_nodes:
            visited_nodes.add(value)  # Visiting current_node for first time
        current_node = current_node.next_element

    start = list2.get_head()

    # Traversing list 2
    # Nodes which are already present in visited_nodes are added to result
    while start:
        value = start.data
        if value in visited_nodes:
            result.insert_at_head(start.data)
        start = start.next_element
    result.remove_duplicates()
    return result

def find_nth(lst, n):
    curr_node=lst.get_head()
    count = 0

    length = lst.length() -  n

    if length < 1:
        return -1

    while curr_node.next_element:
        if count == length:
            return curr_node

        count += 1
        curr_node = curr_node.next_element


lst = LinkedList()
lst.insert_at_head(1)
lst.insert_at_head(4)
lst.insert_at_head(3)
lst.insert_at_head(2)
lst.print_list()
delete(lst, 4)
lst.print_list()
