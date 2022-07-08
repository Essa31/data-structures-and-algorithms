# Python program to for tree traversals

# A class that represents an individual node in a
# Binary Tree





class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinaryTree:
    """
    Define a method for each type of the Depth-first-Tree
    """
    def __init__(self):
        self.root = None

    def insert(self, ro, key):
        self.root=ro
        if self.root is None:
            return Node(key)
        else:
            if self.root.value == key:
                return self.root
            elif self.root.value < key:
                self.root.right = self.insert( self.root.right, key)
            else:
                self.root.left = self.insert( self.root.left, key)
        return  self.root

    def pre_order(self):
        """
        get the nodes from tree in depth-first root-left-right
        """
        if not self.root:
            return self.root

        def traverse(node, current_list):
            """
            store the value of nodes recursively
            """
            if node:
                current_list.append(node.value)
                if node.left is not None:
                    traverse(node.left, current_list)
                if node.right is not None:
                    traverse(node.right, current_list)
            return current_list

        pre_order_list = []
        traverse(self.root, pre_order_list)
        return pre_order_list

    def in_order(self):
        """
        get the nodes from tree in depth-first left-root-right
        """
        if not self.root:
            return self.root

        def traverse(node, current_list):
            """
            store the value of nodes recursively
            """
            if node.left is not None:
                traverse(node.left, current_list)
            current_list.append(node.value)
            if node.right is not None:
                traverse(node.right, current_list)
            return current_list

        in_order_list = []
        traverse(self.root, in_order_list)
        return in_order_list

    def post_order(self):
        """
        get the nodes from tree in depth-first left-right-root
        """
        def traverse(node, current_list):
            """
            store the value of nodes recursively
            """
            if node.left is not None:
                traverse(node.left, current_list)
            if node.right is not None:
                traverse(node.right, current_list)
            current_list.append(node.value)
            return current_list

        post_order_list = []
        traverse(self.root, post_order_list)
        return post_order_list

    def __str__(self):
        if self.root is None:
            return 'None'
        else:
            res_list = self.pre_order()
            output = ''
            for i in res_list:
                output += f'{i}'
            return output

    def find_max(self):
        if self.root is None:
            return None

        def traverse(root, maximum=0):
            if root is None:
                return maximum

            if maximum < root.value:
                maximum = root.value
            left_of_tree = traverse(root.left, maximum)
            if maximum < left_of_tree:
                maximum = left_of_tree
            right_of_tree = traverse(root.right, maximum)
            if maximum < right_of_tree:
                maximum = right_of_tree


            return maximum


        return traverse(self.root)






class BinarySearchTree(BinaryTree):
    """
    this class is a  subclass of the BinaryTree class with Add and Contain methods
    """
    def __init__(self):
        super().__init__()
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        cur_node = self.root
        added_to_tree = False
        while not added_to_tree:
            if cur_node.value >= value:
                if cur_node.left is None:
                    cur_node.left = Node(value)
                    added_to_tree = True
                else:
                    cur_node = cur_node.left
            elif cur_node.value < value:
                if cur_node.right is None:
                    cur_node.right = Node(value)
                    added_to_tree = True
                else:
                    cur_node = cur_node.right

    def contains(self, value):
        bool_res = False
        cur_node = self.root
        while not bool_res:
            if cur_node.value == value:
                return True
            elif cur_node.value > value:
                if cur_node.left is None:
                    bool_res = True
                else:
                    cur_node = cur_node.left
            elif cur_node.value < value:
                if cur_node.right is None:
                    bool_res = True
                else:
                    cur_node = cur_node.right
        return False



