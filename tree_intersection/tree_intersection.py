class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Node:
    """
    Node Instructor.
    This class will have only an __init__ method to create nodes.
    """

    def __init__(self, value, next=None):
        """
        Node Constructor.
            :param value: value of the node
            :param next: reference of next node in line
        """
        self.value = value
        self.next = next


class BinaryTree:
    def __init__(self):
        self.root = None

    def in_order(self):
        """
        Returns the tree nodes in the following order: left >> root >> right
        :return: string
        """
        output = []
        if not self.root:
            return self.root

        def walk(root, out):

            if root.left:
                walk(root.left, out)

            out.append(root.value)

            if root.right:
                walk(root.right, out)

        walk(self.root, output)
        return output


class LinkedList:
    """
    A Linked List class with a single head node
    """

    def __init__(self):
        """
        Singly linked list constructor.
        """
        self.head = None

    def insert(self, value):
        """
        This method will insert a node at the start of the linked list
            :param value: Value to insert
            :return: None
        """
        node = Node(value)
        node.next = self.head
        self.head = node


class HashTable:
    """
    HashTable class will have multiple methods, set, get,
    contains, keys and hash.
    It is a data structure that uses keys and values to store
    data to provide easy and fast access to its items.
    """

    def __init__(self, size=1024):
        """
        HashTable constructor.
            :param size: the size of the data structure
        """
        self.__size = size
        self.__buckets = [None] * size
        self.__keys = []

    def __hash(self, key):
        """
        This method returns the index in the collection of buckets for that key
            :param key: key to reference can be string, number, etc...
            :return: number
        """

        return sum([ord(i) for i in key]) * 283 % self.__size

    def set(self, key, value):
        """
        this method will  hash the key and set the value and key pair in the buckets, also handling the collisions as needed.
            :param key: key to reference can be string, number, etc...
            :param value: value of the referenced key
            :return: None
        """

        h_key = self.__hash(key)
        if self.__buckets[h_key] is None:
            h_list = LinkedList()
            self.__buckets[h_key] = h_list
        self.__keys.append(key)
        self.__buckets[h_key].insert((key, value))


    def get(self, key):
        """
        Used to find the value that is associated with the passed key.
            :param key: Hash key
            :return: referenced value by passed key
        """
        value = []

        h_key = self.__hash(key)
        linked_list_in_buckets = self.__buckets[h_key]
        if linked_list_in_buckets is None:
            return None

        current = linked_list_in_buckets.head
        while current:
            if current.value[0] == key:

                value.append(current.value[1])
            current = current.next

        if len(value) > 1:
            return tuple(value)

        else:
            return value[0]

    def contains(self, key):
        """
        Used to find if the value is contained in the Hash Table or not.
            :param key: key to reference can be string, number, etc...
            :return: bool
        """

        if self.get(key):
          return True

        return False

    def keys(self):
        """
        this method will return a collections of all the keys in hashmap as an object
        :return: an array
        """

        return self.__keys

def tree_intersection(tree1, tree2):
    """
    This function finds the common values between the two trees and returns them.
    :param tree1: first tree
    :param tree2: second tree
    :return: string
    """
    hash_map = HashTable()
    tree_1 = tree1.in_order()
    tree_2 = tree2.in_order()


    output = []

    for i in range(len(tree_1)):
        hash_map.set(str(tree_1[i]), "0")
    print(hash_map.keys())
    print(tree_2)
    for i in tree_2:

        if str(i) in hash_map.keys():
            output+= [str(i)]




    return ",".join(output)


b1_tree = BinaryTree()

b1_tree.root = TreeNode(150)
b1_tree.root.left = TreeNode(100)
b1_tree.root.left.left = TreeNode(75)
b1_tree.root.left.right = TreeNode(160)
b1_tree.root.left.right.left = TreeNode(125)
b1_tree.root.left.right.right = TreeNode(175)
b1_tree.root.right = TreeNode(250)
b1_tree.root.right.left = TreeNode(200)
b1_tree.root.right.right = TreeNode(350)
b1_tree.root.right.right.left = TreeNode(300)
b1_tree.root.right.right.right = TreeNode(500)

b2_tree = BinaryTree()

b2_tree.root = TreeNode(42)
b2_tree.root.left = TreeNode(100)
b2_tree.root.left.left = TreeNode(15)
b2_tree.root.left.right = TreeNode(160)
b2_tree.root.left.right.left = TreeNode(125)
b2_tree.root.left.right.right = TreeNode(175)
b2_tree.root.right = TreeNode(600)
b2_tree.root.right.left = TreeNode(200)
b2_tree.root.right.right = TreeNode(350)
b2_tree.root.right.right.left = TreeNode(4)
b2_tree.root.right.right.right = TreeNode(500)

print(tree_intersection(b1_tree, b2_tree))


