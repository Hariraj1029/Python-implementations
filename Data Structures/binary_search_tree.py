# Define a class for the nodes in the tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

# Define a class for the binary search tree
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a new node into the tree
    def insert(self, value):
        # If the tree is empty, create a new root node
        if self.root is None:
            self.root = Node(value)
        else:
            # Otherwise, find the correct position for the new node
            current_node = self.root
            while True:
                if value < current_node.value:
                    if current_node.left_child is None:
                        current_node.left_child = Node(value)
                        break
                    else:
                        current_node = current_node.left_child
                else:
                    if current_node.right_child is None:
                        current_node.right_child = Node(value)
                        break
                    else:
                        current_node = current_node.right_child

    # Search for a node with a given value
    def search(self, value):
        current_node = self.root
        while current_node is not None:
            if value == current_node.value:
                return True
            elif value < current_node.value:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        return False

    # Delete a node with a given value
    def delete(self, value):
        # Find the node to be deleted
        current_node = self.root
        parent_node = None
        while current_node is not None:
            if value == current_node.value:
                break
            elif value < current_node.value:
                parent_node = current_node
                current_node = current_node.left_child
            else:
                parent_node = current_node
                current_node = current_node.right_child

        # If the node was not found, return
        if current_node is None:
            return

        # If the node has no children, simply remove it
        if current_node.left_child is None and current_node.right_child is None:
            if current_node == self.root:
                self.root = None
            else:
                if parent_node.left_child == current_node:
                    parent_node.left_child = None
                else:
                    parent_node.right_child = None

        # If the node has one child, replace it with its child
        elif current_node.left_child is None:
            if current_node == self.root:
                self.root = current_node.right_child
            else:
                if parent_node.left_child == current_node:
                    parent_node.left_child = current_node.right_child
                else:
                    parent_node.right_child = current_node.right_child
        elif current_node.right_child is None:
            if current_node == self.root:
                self.root = current_node.left_child
            else:
                if parent_node.left_child == current_node:
                    parent_node.left_child = current_node.left_child
                else:
                    parent_node.right_child = current_node.left_child

        # If the node has two children, replace it with its successor
        else:
            successor = current_node.right_child
            successor_parent = current_node
            while successor.left_child is not None:
                successor_parent = successor
                successor = successor.left_child

            if current_node == self.root:
                self.root = successor
            else:
                if parent_node.left_child == current_node:
                    parent_node.left_child = successor
                else:
                    parent_node.right_child = successor

            successor.left_child = current_node.left_child
            if successor != current_node.right_child:
                successor_parent.left_child = successor.right_child
                successor.right_child = current_node.right_child

    # Traverse the tree in order and return a list of values
    def in_order_traversal(self):
        result = []
        self._in_order_traversal(self.root, result)
        return result

    def _in_order_traversal(self, node, result):
        if node is not None:
            self._in_order_traversal(node.left_child, result)
            result.append(node.value)
            self._in_order_traversal(node.right_child, result)

    # Traverse the tree pre-order and return a list of values
    def pre_order_traversal(self):
        result = []
        self._pre_order_traversal(self.root, result)
        return result
    
    def _pre_order_traversal(self, node, result):
        if node is not None:
            result.append(node.value)
            self._pre_order_traversal(node.left_child, result)
            self._pre_order_traversal(node.right_child, result)

    # Traverse the tree post-order and return a list of values
    def post_order_traversal(self):
        result = []
        self._post_order_traversal(self.root, result)
        return result
    
    def _post_order_traversal(self, node, result):
        if node is not None:
            self._post_order_traversal(node.left_child, result)
            self._post_order_traversal(node.right_child, result)
            result.append(node.value)

    # Find the minimum value in the tree
    def find_min(self):
        current_node = self.root
        while current_node.left_child is not None:
            current_node = current_node.left_child
        return current_node.value
    
    # Find the maximum value in the tree
    def find_max(self):
        current_node = self.root
        while current_node.right_child is not None:
            current_node = current_node.right_child
        return current_node.value
    
    # Calculate the height of the tree
    def calculate_height(self):
        return self._calculate_height(self.root)
    
    def _calculate_height(self, node):
        if node is None:
            return -1
        return 1 + max(self._calculate_height(node.left_child), self._calculate_height(node.right_child))
    
    # Check if the tree is a binary search tree
    def is_binary_search_tree(self):
        return self._is_binary_search_tree(self.root, float("-inf"), float("inf"))
    
    def _is_binary_search_tree(self, node, min_value, max_value):
        if node is None:
            return True
        if node.value < min_value or node.value > max_value:
            return False
        return self._is_binary_search_tree(node.left_child, min_value, node.value) and self._is_binary_search_tree(node.right_child, node.value, max_value)
    
    # Delete the entire tree
    def delete_tree(self):
        self.root = None

# Create a binary search tree
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(4)
bst.insert(6)
bst.insert(8)

# Test search
print(bst.search(4)) # True
print(bst.search(10)) # False

# Test delete
bst.delete(8)
print(bst.search(8)) # False

# Test in-order traversal
print(bst.in_order_traversal()) # [1, 3, 4, 5, 6, 7]

# Test pre-order traversal
print(bst.pre_order_traversal()) # [5, 3, 1, 4, 7, 6]

# Test post-order traversal
print(bst.post_order_traversal()) # [1, 4, 3, 6, 7, 5]

# Test minimum and maximum
print(bst.find_min()) # 1
print(bst.find_max()) # 7

# Test height
print(bst.calculate_height()) # 2

# Test deletion of entire tree
bst.delete_tree()
print(bst.in_order_traversal()) # []

# Test if binary search tree
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(4)
bst.insert(6)
bst.insert(8)
print(bst.is_binary_search_tree()) # True

bst.root.left_child.right_child.value = 10
print(bst.is_binary_search_tree()) # False

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
