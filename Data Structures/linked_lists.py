class Node: # Node class
    def __init__(self, data):   # Constructor to initialize the node object
        self.data = data    # Assign data
        self.next = None    # Initialize next as null

class LinkedList:   # LinkedList class
    def __init__(self): # Constructor to initialize the linked list object
        self.head = None    # Initialize head as null

    def append(self, data): # Function to insert a new node at the end of the linked list
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):    # Function to insert a new node at the beginning of the linked list
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):   # Function to insert a new node after a given node
        if not prev_node:
            print("Previous node is not in the list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key): # Function to delete a node with a given key
        curr_node = self.head
        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return
        prev_node = None
        while curr_node and curr_node.data != key:
            prev_node = curr_node
            curr_node = curr_node.next
        if curr_node is None:
            return
        prev_node.next = curr_node.next
        curr_node = None

    def delete_node_at_pos(self, pos):  # Function to delete a node at a given position
        curr_node = self.head
        if pos == 0:
            self.head = curr_node.next
            curr_node = None
            return
        prev_node = None
        count = 0
        while curr_node and count != pos:
            prev_node = curr_node
            curr_node = curr_node.next
            count += 1
        if curr_node is None:
            return
        prev_node.next = curr_node.next
        curr_node = None

    def length_iterative(self): # Function to get the length of the linked list iteratively
        count = 0
        curr_node = self.head
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count

    def length_recursive(self, node):   # Function to get the length of the linked list recursively
        if node is None:
            return 0
        return 1 + self.length_recursive(node.next)

    def swap_nodes(self, key1, key2):   # Function to swap two nodes
        if key1 == key2:
            return
        prev1 = None
        curr1 = self.head
        while curr1 and curr1.data != key1:
            prev1 = curr1
            curr1 = curr1.next
        prev2 = None
        curr2 = self.head
        while curr2 and curr2.data != key2:
            prev2 = curr2
            curr2 = curr2.next
        if not curr1 or not curr2:
            return
        if prev1:
            prev1.next = curr2
        else:
            self.head = curr2
        if prev2:
            prev2.next = curr1
        else:
            self.head = curr1
        curr1.next, curr2.next = curr2.next, curr1.next

    def reverse_iterative(self):    # Function to reverse a linked list iteratively
        prev_node = None
        curr_node = self.head
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node

    def reverse_recursive(self):    # Function to reverse a linked list recursively
        def _reverse_recursive(curr_node, prev_node):
            if not curr_node:
                return prev_node
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
            return _reverse_recursive(curr_node, prev_node)
        self.head = _reverse_recursive(curr_node=self.head, prev_node=None)

    def print_list(self):   # Function to print the linked list
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    def print_helper(self, node, name): # Function to print the linked list in a specific format
        if node is None:
            print(name + ": None")
        else:
            print(name + ":" + node.data)

    def merge_sorted(self, llist):  # Function to merge two sorted linked lists
        p = self.head
        q = llist.head
        s = None
        if not p:
            return q
        if not q:
            return p
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p
        return new_head
    
    def remove_duplicates(self):    # Function to remove duplicates from a sorted linked list
        curr_node = self.head
        prev_node = None
        dup_values = dict()
        while curr_node:
            if curr_node.data in dup_values:
                prev_node.next = curr_node.next
                curr_node = None
            else:
                dup_values[curr_node.data] = 1
                prev_node = curr_node
            curr_node = prev_node.next

    def print_nth_from_last(self, n):   # Function to print the nth node from the end of a linked list
        total_len = self.length_iterative()
        curr_node = self.head
        while curr_node:
            if total_len == n:
                print(curr_node.data)
                return curr_node
            total_len -= 1
            curr_node = curr_node.next
        if curr_node is None:
            return 
        
    def print_nth_from_last2(self, n):  # Function to print the nth node from the end of a linked list
        p = self.head
        q = self.head
        count = 0
        while q and count < n:
            q = q.next
            count += 1
        if not q:
            print(str(n) + " is greater than the number of nodes in the list.")
            return
        while p and q:
            p = p.next
            q = q.next
        return p.data
    
    def count_occurences_iterative(self, data): # Function to count the number of occurrences of a given element in a linked list iteratively
        count = 0
        curr_node = self.head
        while curr_node:
            if curr_node.data == data:
                count += 1
            curr_node = curr_node.next
        return count
    
    def count_occurences_recursive(self, node, data):    # Function to count the number of occurrences of a given element in a linked list recursively
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurences_recursive(node.next, data)
        else:
            return self.count_occurences_recursive(node.next, data)
        
    def rotate(self, k):    # Function to rotate a linked list
        p = self.head
        q = self.head
        prev_node = None
        count = 0
        while p and count < k:
            prev_node = p
            p = p.next
            q = q.next
            count += 1
        p = prev_node
        while q:
            prev_node = q
            q = q.next
        q = prev_node
        q.next = self.head
        self.head = p.next
        p.next = None

    def is_palindrome1(self):   # Function to check if a linked list is a palindrome
        s = ""
        p = self.head
        while p:
            s += p.data
            p = p.next
        return s == s[::-1]
    
    def is_palindrome2(self):   # Function to check if a linked list is a palindrome
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
    
    def is_palindrome3(self):   # Function to check if a linked list is a palindrome
        p = self.head
        q = self.head
        prev_node = []
        i = 0
        while q:
            prev_node.append(q)
            q = q.next
            i += 1
        q = prev_node[i-1]
        count = 1
        while count <= i//2 + 1:
            if prev_node[-count].data != p.data:
                return False
            p = p.next
            count += 1
        return True
    
    def move_tail_to_head(self):    # Function to move the last element to the front of a linked list
        last = self.head
        second_to_last = None
        while last.next:
            second_to_last = last
            last = last.next
        last.next = self.head
        second_to_last.next = None
        self.head = last

    def sum_two_lists(self, llist): # Function to add two linked lists
        p = self.head
        q = llist.head
        sum_list = LinkedList()
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
                sum_list.append(remainder)
            else:
                carry = 0
                sum_list.append(s)
            if p:
                p = p.next
            if q:
                q = q.next
        sum_list.print_list()

    def remove_duplicates(self):    # Function to remove duplicates from a linked list
        prev = None
        curr = self.head
        dup_values = dict()
        while curr:
            if curr.data in dup_values:
                prev.next = curr.next
                curr = None
            else:
                dup_values[curr.data] = 1
                prev = curr
            curr = prev.next


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("E")

llist.remove_duplicates()
llist.print_list()

llist1 = LinkedList()
llist1.append(1)
llist1.append(5)
llist1.append(7)
llist1.append(9)
llist1.append(10)

llist2 = LinkedList()
llist2.append(2)
llist2.append(3)
llist2.append(4)
llist2.append(6)
llist2.append(8)

llist1.merge_sorted(llist2)
llist1.print_list()

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("E")
llist.append("F")
llist.rotate(4)
llist.print_list()

llist = LinkedList()
llist.append("R")
llist.append("A")
llist.append("D")
llist.append("A")
llist.append("R")
print(llist.is_palindrome1())
print(llist.is_palindrome2())
print(llist.is_palindrome3())

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("E")
llist.move_tail_to_head()
llist.print_list()

llist1 = LinkedList()
llist1.append(5)
llist1.append(6)
llist1.append(3)

llist2 = LinkedList()
llist2.append(8)
llist2.append(4)
llist2.append(2)

llist1.sum_two_lists(llist2)
