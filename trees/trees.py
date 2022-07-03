# Python program to for tree traversals

# A class that represents an individual node in a
# Binary Tree


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree():
    # A function to do inorder tree traversal
    def In_order(self,root):

        if root:
            # First recur on left child
            self.In_order(root.left)

            # then print the data of node
            print(root.val,end="->"),


            # now recur on right child
            self.In_order(root.right)
        return



    # A function to do postorder tree traversal
    def Post_order(self,root):
        if root:
            # First recur on left child
            self.Post_order(root.left)

            # the recur on right child
            self.Post_order(root.right)

            # now print the data of node
            print(root.val,end="->"),



    # A function to do preorder tree traversal
    def Pre_order(self,root):
        if root:
            # First print the data of node
            print(root.val , end="->"),

            # Then recur on left child
            self.Post_order(root.left)

            # Finally recur on right child
            self.Post_order(root.right)

class BinarySearchTree(BinaryTree):

    def Add(self,val):

        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = Node(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = Node(val)
        return


    def Contains(root,value):


        if root.value == value:
            return True
        elif root.value < value:
            return root.right.value == value
        else:
            return root.right.value == value



# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

a=BinaryTree()

a.Pre_order(root)

print("\n")

a.In_order(root)

print("\n")

a.Post_order(root)
c=BinarySearchTree()
c.Contains(3)

