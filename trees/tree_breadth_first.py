class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinaryTree:

    def __init__(self):
        self.root = None


    def breadth_first(self,root):
        visit=[]
        rot=[]
        if root!=None:
            current = root
            rot+=[current]

            try:
                while rot!=[]:
                    rot+=[rot[0].left]
                    rot+=[rot[0].right]
                    visit+=[rot[0].value]
                    del rot[0]
            except:

                return visit
        else:
            raise Exception("tree is empty")

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

    def maxValue(self):
        if self.root!=None:
            current = self.root


            while (current.right):
                current = current.right
            return current.value
        else:
            raise Exception("tree is empty")

trees=BinaryTree()
root = Node(1)
root.left = Node(6)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(5)
print(trees.breadth_first(root))