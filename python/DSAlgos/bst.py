
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):

        node = Node(new_val)
        curr_node = self.root
        while True:

            if curr_node.value < new_val:
                if curr_node.right:
                    curr_node = curr_node.right
                    continue
                else:
                    curr_node.right = node
                    return
            else:
                if curr_node.left:
                    curr_node = curr_node.left
                else:
                    curr_node.left = node
                    return

    def search(self, find_val):

        curr_node = self.root
        while True:
            if curr_node.value == find_val:
                return True

            if curr_node.value < find_val:
                if curr_node.right:
                    curr_node = curr_node.right
                    continue
                else:
                    return False
            else:
                if curr_node.left:
                    curr_node = curr_node.left
                else:
                    return False


                # Set up tree

tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))