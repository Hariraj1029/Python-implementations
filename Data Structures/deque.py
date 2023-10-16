class Deque:
    def __init__(self):
        self.items = []  # Initialize an empty list to store the deque items

    def is_empty(self):
        return self.items == []  # Check if the deque is empty

    def add_front(self, item):
        self.items.append(item)  # Add an item to the front of the deque

    def add_rear(self, item):
        self.items.insert(0, item)  # Add an item to the rear of the deque

    def remove_front(self):
        return self.items.pop()  # Remove and return the item at the front of the deque

    def remove_rear(self):
        return self.items.pop(0)  # Remove and return the item at the rear of the deque

    def size(self):
        return len(self.items)  # Return the number of items in the deque

    def peek_front(self):
        return self.items[-1]   # Peek at the front of the deque
    
    def peek_rear(self):
        return self.items[0]    # Peek at the rear of the deque
    
    def __str__(self):
        return str(self.items)  # String representation of the items   
    
    def __len__(self):
        return len(self.items)  # Length of the deque
    
    def __contains__(self, item):
        return item in self.items   # Check if an item is in the deque
    
    def __iter__(self):
        return iter(self.items)     # Iterate over the deque items
    
    def __getitem__(self, index):
        return self.items[index]    # Get an item from the deque by index
    
    def __setitem__(self, index, item):
        self.items[index] = item    # Set an item in the deque by index

# Create a deque

deque = Deque()
print(deque.is_empty())  # True
deque.add_front(1)  # deque = [1]
deque.add_front(2)  # deque = [2, 1]
deque.add_rear(3)  # deque = [2, 1, 3]
deque.add_rear(4)  # deque = [2, 1, 3, 4]
print(deque)  # [2, 1, 3, 4]
print(deque.size())  # 4
print(deque.is_empty())  # False
print(deque.peek_front())  # 4
print(deque.peek_rear())  # 2
print(deque.remove_front())  # 4
print(deque.remove_rear())  # 2
print(deque)  # [1, 3]

    
# using deque from collections module
from collections import deque

# Create a deque
deque = deque()
print(deque)  # deque([])
deque.append(1)  # deque = [1]
deque.append(2)  # deque = [1, 2]
deque.appendleft(3)  # deque = [3, 1, 2]
deque.appendleft(4)  # deque = [4, 3, 1, 2]
print(deque)  # deque([4, 3, 1, 2])
print(deque.pop())  # 2
print(deque.popleft())  # 4
print(deque)  # deque([3, 1])
print(deque.count(3))  # 1
print(deque.index(3))  # 0
deque.reverse()  # deque = [1, 3]
deque.rotate(1)  # deque = [3, 1]
deque.rotate(-1)  # deque = [1, 3]
deque.clear()  # deque = []
deque.extend([1, 2, 3])  # deque = [1, 2, 3]
deque.extendleft([4, 5, 6])  # deque = [6, 5, 4, 1, 2, 3]
deque.remove(6)  # deque = [5, 4, 1, 2, 3]
deque.insert(2, 6)  # deque = [5, 4, 6, 1, 2, 3]
deque.insert(-1, 7)  # deque = [5, 4, 6, 1, 2, 7, 3]
deque.remove(7)  # deque = [5, 4, 6, 1, 2, 3]
