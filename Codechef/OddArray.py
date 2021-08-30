def arr(left,right,res,n,m):
    if(left>right):
        return
    mid=(left+right)//2
    res[mid]=m
    arr(left,mid-1,res,n,m+1)
    arr(mid+1,right,res,n,m+1)

def main():
    for _ in range(int(input())):
        n=int(input())
        res=[0]*n
        arr(0,n-1,res,n,1)
        print(*res)
if __name__=="__main__":
    main()

