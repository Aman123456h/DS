class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def insert_beg(self,data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb

    def insert_end(self,data):
        ne = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne

    def insert_pos(self,pos,data):
        np = Node(data)
        temp = self.head
        for i in range(pos-1):
            temp = temp.next
        np.next = temp.next
        temp.next = np

    def remove_beg(self):
        temp = self.head
        self.head = temp.next
        temp=None

    def remove_end(self):
        temp = self.head
        prev=self.head.next
        while prev.next:
            temp=temp.next
            prev=prev.next
        temp.next=None

    def remove_pos(self,pos):
        temp = self.head
        prev = self.head.next
        for i in range(pos-1):
            temp = temp.next
            prev = prev.next
        temp.next = prev.next
        prev.next = None

    def display(self):
        if self.head==None:
            print("Linked List is Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data,"--->",end=" ")
                temp = temp.next
            print("None")

l = SLL()
n = Node(52)
l.head = n
n1 = Node(10)
n.next = n1
l.display()
l.insert_beg(20)
l.display()
n2 = Node(53)
n1.next = n2
l.display()
l.insert_end(49)
l.display()
l.insert_pos(2,50)
l.display()
l.remove_beg()
l.display()
l.remove_end()
l.display()
l.remove_pos(2)
l.display()
