t=int(input())
while(t):
    n=int(input())
    res=[]
    arr=[int(i) for i in input().split()]
    for i in range(n):
        res.append([arr[i],True])
    for i in range(n):
        for j in range(i):
            if(res[j][0]>res[j+1][0]):
                temp=res[j][0]
                res[j][0]=res[j+1][0]
                res[j+1][0]=temp
                res[j][1]=not res[j][1]
                res[j+1][1]=not res[j+1][1]
    print(res)
    t-=1