class sll():
    def __init__(self):
        self.head=None
        self.length=0
    def displayLength(self):
        if self.head==None:
            print("Empty list")
        else:
            temp=self.head
            while temp:
                temp=temp.next
                self.length+=1
            print(f'The list is {self.length} long')
    def display(self):
        if self.head==None:
            print("Empty list")
        else:
            temp=self.head
            while temp:
                print(temp.data, "->", end= ' ')
                temp=temp.next
            print("None")
    def deleteLast(self):
        if self.head==None:
            print("Empty list")
        else:
            temp=self.head
            while temp.next and temp.next.next:
                    temp=temp.next
            del(temp.next)
            temp.next=None
            
    def deleteFirst(self):
        self.head=self.head.next
    def deletePos(self, position):
        count=0
        temp=self.head
        while temp:
            if position==count:
                temp.next=temp.next.next
            else:
                temp=temp.next
            count+=1
    def incertFirst(self,node):
        if self.head==None:
            print("Empty list")
        else:
            temp=self.head
            self.head=node
            self.head.next=temp
    def incertLast(self, node):
        temp=self.head
        while temp:
            if temp.next==None:
                temp.next=node
                temp.next.next=None
                break
            temp=temp.next
    def incertPost(self, node, pos):
        pos-=1
        count=0
        if self.head==None:
            print("Empty list")
        else:
            temp=self.head
            while temp:
                if pos==count:
                    pass
                count+=1
        
            
        
    
class node():
    def __init__(self, data):
        self.data=data
        self.next=None




n1=node(1)
n2=node(2)
n3=node(3)
l=sll()
l.head=n3
n3.next=n1
n1.next=n2
l.display()
