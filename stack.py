class Node:
    def __init__(self,data):
        self.data=data
        self.next = None

class stack:
    def __init__(self):
        self.top = None

    def push(self):
        n = int(input("Enter the Elements: "))
        ne = Node(n)
        if self.top is None:
            self.top = ne
            self.top.next = None
        else:
            ne.next = self.top
            self.top = ne

    def pop(self):
        if self.top is None:
            print("The Stack is Empty")
        elif self.top.next is None:
            print("The popped Element is: ",self.top.data)
            self.top=None
        else:
            temp =self.top
            self.top = temp.next
            temp = None

    def display(self):
        if self.top is None:
            print("The Stack is Empty")
        else:
            temp = self.top
            print("The Element of the Stack is")
            while temp:
                print(temp.data)
                temp=temp.next
            print("Top is: ",self.top.data)

s = stack()
while True:
    print("1.Push Operation\n2.Pop Operation\n3.Display Operation")
    n = int(input())
    if n==1:
        s.push()
    elif n==2:
        s.pop()
    elif n==3:
        s.display()
    else:
        break
        

        
