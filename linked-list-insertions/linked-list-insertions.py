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



    def includes (self,value):
        concurrent = self.head
        while concurrent:
            if concurrent.value == value:
                return True
            else:
                concurrent=concurrent.next
        return False


    def Insert_After(self, position, newElement):
            node = Node(newElement)


            if self.head  == None:
                self.head = node
            else:
                concurrent = self.head
                try:
                    while concurrent.value != position:


                        concurrent = concurrent.next
                    if concurrent.next==None:
                        concurrent.next=node
                    else:

                        node.next = concurrent.next

                        concurrent.next = node
                except:
                    print( "No change, method exception")





    def Insert_Before(self,position, newElement):

        node = Node(newElement)

        if self.head == None:
            self.head = node
        else:
            concurrent = self.head
            try:
                while concurrent.next.value != position:
                    concurrent = concurrent.next

                node.next=concurrent.next

                concurrent.next=node



            except:
                print("No change, method exception")






     




    def to_string(self):
            concurrent=self.head
            item=""
            while concurrent:
                item+=f'<{concurrent.value}> -- >'
                concurrent=concurrent.next
            item += "Null"
            return item



a=linkedlist()


a.append(1)
a.append(3)
a.append(2)
# a.append(4)
# a.append(5)


# print(a.to_string())
a.Insert_After(3, 5)

# print(a.to_string())
# a.Insert_Before(3, 5)
# print(a.to_string())
