class Node :
    def __init__(self,value):
        self.value=value
        self.next=None

class linkedlist:
    def __init__(self):
       self.head=None


    def insert (self,value):
        node = Node(value)
        print(node.value)


        node.next = self.head
        print(node.next)


        self.head = node










    def to_string(self):
        concurrent=self.head
        item=""
        while concurrent:
            item+=f'<{concurrent.value}> -- >'
            concurrent=concurrent.next
        item += "Null"
        return item



    def includes (self,value):
        concurrent = self.head
        while concurrent:
            if concurrent.value == value:
                return True
            else:
                concurrent=concurrent.next
        return False






a=linkedlist()


a.insert(1)
a.insert(2)
a.insert(3)
a.insert(4)
a.insert(5)
print(a.to_string())
print(a.includes(5))
