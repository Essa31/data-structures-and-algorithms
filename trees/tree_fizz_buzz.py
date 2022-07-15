class K_Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class K_Tree:

    def __init__(self):
        self.root = None

    def __str__(self):
        if self.root is None:
            return 'None'
        else:
            res_list = self.pre_order()
            output = ''
            for i in res_list:
                output += f'{i}'
            return output
    def print_tree_as_arr(self,root):
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

def fizz_buzz_tree(root):

    rot = []
    if root != None:
        current = root
        rot += [current]

        try:
            while rot != []:
                rot += [rot[0].left]
                rot += [rot[0].right]

                if rot[0].value%3==0 and rot[0].value%5==0:
                   rot[0].value="FizzBuzz"


                elif rot[0].value % 3 == 0 :
                    rot[0].value= "Fizz"


                elif rot[0].value % 5 == 0 :
                    rot[0].value="Buzz"



                    del rot[0]
        except:

            return root
    else:
        raise Exception("tree is empty")

trees=K_Tree()
root = K_Node(7)
root.left = K_Node(6)
root.right = K_Node(8)
root.left.left = K_Node(21)
root.left.right = K_Node(5)
print(trees.fizz_buzz_tree(root))
print(trees.print_tree_as_arr(root))

