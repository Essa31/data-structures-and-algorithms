def z(l1, l2):
    c1 = l1.head.next
    c2 = l2.head.next

    curr1 = l1.head
    curr2 = l2.head
    while curr1 and curr2 :

        curr1.next = curr2
        curr2.next = c1

        curr1 = c1
        curr2 = c2
        c1 = c1.next
        c2 = c2.next
    return l1

    # curr2.next = curr2
    # curr2.next = c1
    # c1 = c1.next



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

        while p_curr != None and q_curr != None:
            p_next = p_curr.next
            q_next = q_curr.next

            q_curr.next = p_next
            p_curr.next = q_curr

            p_curr = p_next
            q_curr = q_next
            q.head = q_curr

        concurrent = q_curr

        while concurrent != None:
            p_curr.append(concurrent.value)
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
a.append(3)
a.append(2)

d = linkedlist()

d.append(0)
d.append(0)
d.append(0)
# d.append(0)
z(a, d)
print(a.to_string())
