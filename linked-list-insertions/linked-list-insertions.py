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





    def insert_before(self,given_ptr,val):

            global head


            if head == given_ptr:


                n = Node(val)


                n.next = head


                head = n
                return n


            else:

                p = None
                n = head


                while (n != given_ptr):
                    p = n
                    n = n.next

                # Create a node
                m = Node(val)

                # Update the m.next
                m.next = p.next

                # Update previous node's next
                p.next = m

            return m

    def insert_After(self, prev_node, new_data):

        node = Node(new_data)
        if self.head == None:
            self.head = node
        else:
            concurrent = self.head
            while concurrent.next != prev_node:
                concurrent = concurrent.next
                print("hello")
            concurrent.next

            concurrent.next = node







    def to_string(self):
            concurrent=self.head
            item=""
            while concurrent:
                item+=f'<{concurrent.value}> -- >'
                concurrent=concurrent.next
            item += "Null"
            return item

    def includes(self, value):
        concurrent = self.head
        while concurrent:
            if concurrent.value == value:
                return True
            else:
                concurrent = concurrent.next
        return False

a=linkedlist()


a.append(1)
a.append(3)
a.append(2)
# a.append(4)
# a.append(5)


print(a.to_string())
print(a.insert_After(3,5))
print(a.to_string())
# print(a.insert_before(3, 5))