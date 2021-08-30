class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def leftView(root,level,maxlevel):
    if root is None:
        return
    if(maxlevel[0]<level):
        print(root.data,end=" ")
        maxlevel[0]=level
    leftView(root.left,level+1,maxlevel)
    leftView(root.right,level+1,maxlevel)

if __name__=="__main__":
    root=Node(10)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(7)
    root.left.right=Node(8)
    root.right.right=Node(15)
    root.right.left=Node(12)
    root.right.right.left=Node(14)
    leftView(root,1,[0])