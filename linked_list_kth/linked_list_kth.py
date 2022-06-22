
class Node :
    def __init__(self,value):
        self.value=value
        self.next=None

class linkedlist:




    def __init__(self):
       self.head=None


    def append (self,value):
        node = Node(value)
        if self.head==None:
            self.head=node
        else:
            concurrent=self.head
            while concurrent.next != None:
                concurrent=concurrent.next
            concurrent.next



            concurrent.next = node




    def kth_From_End(self,k):
        concurrent = self.head
        item = []
        while concurrent:
            item += f'{concurrent.value}'
            concurrent = concurrent.next
        x=item[::-1]
        l=len(item)
        if k >= 0:
            if k <= l-1 :
                return x[k]
            else:
                return "Exception"

        else:
            return "Exception"



a=linkedlist()


a.append(1)
a.append(3)
a.append(8)
a.append(2)

print(a.kth_From_End(0))
print(a.kth_From_End(-2))
print(a.kth_From_End(-6))
