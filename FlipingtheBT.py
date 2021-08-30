"""
(Recursive Approach)
Main Part:-

def flipBT(root):
    if root==None:
        return root
    if root.left == None and root.right == None:
        return root
    fliproot = flipBT(root.left)
    root.left.left=root.right
    root.left.right=root
    root.left=root.right=None
    return fliproot

(Itterative Approach)
Main Part:-

def flipBT(root):
    curr=root
    next=None
    temp=None
    prev=None
    while(curr):
        next=curr.left
        curr.left=temp
        temp=curr.right
        curr.right = prev
        prev = curr
        curr = next
    return prev


"""