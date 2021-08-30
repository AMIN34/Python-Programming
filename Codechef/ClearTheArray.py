for _ in range(int(input())):
    n,k,x=map(int, input().split())
    arr=list(map(int,input().split()))
    arr.sort()
    cost=0
    while(k>0 and len(arr)>1):
        sumc = arr[-1]+arr[-2]
        if(sumc>=x):
            arr.pop(-1)
            arr.pop(-1)
            cost+=x
            k-=1
        else: break
    cost+=sum(arr)
    print(cost)