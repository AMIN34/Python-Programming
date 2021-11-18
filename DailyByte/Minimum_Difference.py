import math
class TreeNode:
    def __init__(self,data) -> None:
        self.val=data
        self.left=self.right=None

def arrayToBST(arr:list):
    if not arr:
        return None
    arr=sorted(arr)
    mid=(len(arr))//2
    root=TreeNode(arr[mid])
    root.left=arrayToBST(arr[:mid])
    root.right=arrayToBST(arr[mid+1:])
    return root

def minDiff(root:TreeNode,target:int)->int:
    if not root:
        return target
    if root.left:
        l = root.val-root.left.val
        target=min(target,l)
    if root.right:
        r=root.right.val-root.val
        target=min(target,r)
    return min(minDiff(root.left,target),minDiff(root.right,target))

def main():
    print("Enter no.of test cases: ",end="")
    for _ in range(int(input())):
        arr=list(map(int, input("Enter array elements: ").split()))
        root=arrayToBST(arr)
        print(minDiff(root,math.inf))

if __name__=="__main__":
    main()

    