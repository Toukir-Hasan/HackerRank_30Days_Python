class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
            p = Node(data)
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        first=second=head
        while first !=None:
            while second.next !=None:
                if second.next.data==first.data:
                    second.next=second.next.next
                else:
                    second=second.next
            first=second=first.next
        return head



mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
head1=mylist.removeDuplicates(head)
mylist.display(head1);



