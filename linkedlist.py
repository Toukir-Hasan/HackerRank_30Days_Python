class node:
    def __init__(self, data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insert(self,newNode):
        if self.head==None:
            self.head=newNode
        else:
            lastNode=self.head
            while lastNode.next!=None:
                lastNode=lastNode.next
            lastNode.next= newNode
    def print(self):
        currentNode=self.head
        while currentNode !=None:
            print(currentNode.data)
            currentNode=currentNode.next

f=node("JJ")
k=linkedlist()
k.insert(f)
s=node("u")
k.insert(s)
d=node("lala")
k.insert(d)
k.print()





