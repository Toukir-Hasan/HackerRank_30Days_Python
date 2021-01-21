class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                print("Left side ",root.data)
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                print("Right side ",root.data)
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        if root==None:
            return -1
        lh=self.getHeight(root.left)
        rh=self.getHeight(root.right)
        return 1 + max(lh,rh)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    print("root is ", root)
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)