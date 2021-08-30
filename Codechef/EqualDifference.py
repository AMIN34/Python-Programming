from collections import defaultdict
for _ in range(int(input())):
    n=int(input())
    frequency = defaultdict(int)
    # arr=[int(i) for i in input().split()][::n]
    arr=map(int,input().split())
    # print(arr)
    m=0
    for item in arr:
        if(item in frequency):
            frequency[item]+=1
            m=max(m,frequency[item])
        else:
            frequency[item]=1
            m=max(m,frequency[item])
    if n<=2:
        print(0)
        continue
    if m==1:
        print(n-2)
    else:
        print(n-m)