
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class linkedlist:

    def __init__(self):
        self.head = None

    def append(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            concurrent = self.head
            while concurrent.next != None:
                concurrent = concurrent.next

            concurrent.next = node

    def zipLists(self, p, q):

        p_curr = p.head
        q_curr = q.head
        if p.head==None or q.head ==None:
            print( "Make sure the linked list is not empty")
            return
        else:
            while p_curr.next != None and q_curr != None:
                p_next = p_curr.next
                q_next = q_curr.next

                q_curr.next = p_next
                p_curr.next = q_curr

                p_curr = p_next
                q_curr = q_next
                q.head = q_curr

            concurrent = q_curr



            while concurrent != None:
                p_curr.next=concurrent
                p_curr=p_curr.next


                concurrent = concurrent.next

    def to_string(self):
        concurrent = self.head
        item = ""
        while concurrent:
            item += f'<{concurrent.value}> -- >'
            concurrent = concurrent.next
        item += "Null"
        return item


a = linkedlist()

a.append(1)
a.append(1)
a.append(1)
a.append(1)


d = linkedlist()

d.append(2)
d.append(3)
d.append(4)
d.append(5)
d.append(6)
a.zipLists(a,d)
print(a.to_string())
