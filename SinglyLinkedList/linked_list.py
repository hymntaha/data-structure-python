class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print('Previous node does not exist')
            return

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):

        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):
        if self.head:
            cur_node = self.head
            if pos == 0:
                self.head = cur_node.next
                cur_node = None
                return

            prev = None
            count = 0
            while pos != count and self.head:
                prev = cur_node
                cur_node = cur_node.next
                count +=1

            if cur_node is None:
                return

            prev.next = cur_node.next
            cur_node = None

    def len_iterative(self):
        if self.head is None:
            return 0

        count = 1
        cur_node = self.head

        while cur_node.next is not None:
            cur_node = cur_node.next
            count += 1

        print(count)

    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return

        prev_1 = None
        curr_1 = self.head

        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head

        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2


        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def reverse_iterative(self):
        prev = None
        cur = self.head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        self.head = prev

    def merge_sorted(self, llist):

        p = self.head
        Q = llist.head
        s = None

        if not p:
            return Q
        if not Q:
            return p

        if p and Q:
            if p.data <= Q.data:
                s = p
                p = s.next
            else:
                s = Q
                q = s.next
            new_head = s

        while p and Q:
            if p.data <= Q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = Q
                s = Q
                Q = s.next
        if not p:
            s.next = Q
        if not Q:
            s.next = p

        return new_head

    def remove_duplicates(self):
        # 1 -> 6 -> 1 -> 4 -> 2 -> 2 -> 4

        cur = self.head
        prev = None
        dup_values = dict()

        while cur:
            if cur.data in dup_values:
                # Remove node:
                prev.next = cur.next
                cur = None
            else:
                # Have not encountered element before.
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.next

    def print_nth_from_last(self, n):
            p = self.head
            q = self.head

            count = 0
            while q:
                count += 1
                if(count>=n):
                    break
                q = q.next

            if not q:
                print(str(n) + " is greater than the number of nodes in list.")
                return

            while p and q.next:
                p = p.next
                q = q.next
            return p.data

    def count_occurences_iterative(self,data):
        count = 0
        cur = self.head
        while cur:
            if cur.data == data:
                count += 1
            cur = cur.next
        return count

    def rotate(self, k):
        if self.head and self.head.next:
            p = self.head
            q = self.head
            prev = None
            count = 0

            while p and count < k:
                prev = p
                p = p.next
                q = q.next
                count += 1

            p = prev
            while q:
                prev = q
                q = q.next
            q = prev

            q.next = self.head
            self.head = p.next
            p.next = None

    def is_palindrome(self):

        p = self.head
        s = []

        while p:
            s.append(p.data)
            p = p.next
        p = self.head

        while p:
            data = s.pop()
            if p.data != data:
                return False
            p = p.next
        return True

    def move_tail_to_head(self):
        if self.head and self.head.next:
            last = self.head
            second_to_last = None
            while last.next:
                second_to_last = last
                last = last.next
            last.next = self.head
            second_to_last.next = None
            self.head = last

    def sum_two_lists(self, llist):
        p = self.head
        q = llist.head

        sum_llist = LinkedList()

        carry = 0
        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                j = 0
            else:
                j = q.data
            s = i + j + carry
            if s >= 10:
                carry = 1
                remainder = s % 10
                sum_llist.append(remainder)
            else:
                carry = 0
                sum_llist.append(s)
            if p:
                p = p.next
            if q:
                q = q.next

        return sum_llist

# llist1 = LinkedList()
# llist1.append(5)
# llist1.append(6)
# llist1.append(3)
#
# llist2 = LinkedList()
# llist2.append(8)
# llist2.append(4)
# llist2.append(2)
#
# print(365 + 248)
# llist1.sum_two_lists(llist2)

# llist.move_tail_to_head()
# llist.print_list()
# print(llist.is_palindrome())

# llist.is_palindrome(4)
# llist.print_list()

# print(llist.count_occurences_iterative(1))

# print(llist.print_nth_from_last(2))
# print(llist.print_nth_from_last(4))

# print("Original Linked List")
# llist.print_list()
# print("Linked List After Removing Duplicates")
# llist.remove_duplicates()
# llist.print_list()

# llist_1 = LinkedList()
# llist_2 = LinkedList()
#
# llist_1.append(1)
# llist_1.append(5)
# llist_1.append(7)
# llist_1.append(9)
# llist_1.append(10)
#
# llist_2.append(2)
# llist_2.append(3)
# llist_2.append(4)
# llist_2.append(6)
# llist_2.append(8)
#
# llist_1.merge_sorted(llist_2)
# llist_1.print_list()

# llist = LinkedList()
# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.reverse_iterative()
# llist.print_list()
# llist.delete_node_at_pos(2)
# llist.delete_node("B")
# llist.delete_node("E")
# print("Original List")
# llist.print_list()
#
#
# llist.swap_nodes("B", "C")
# print("Swapping nodes B and C that are not head nodes")
# llist.print_list()
