import collections
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int, input().split()))
    freq=collections.Counter(arr)
    res = n- freq[0]-freq[1]-freq[-1]
    if res>1:
        print(0)
        continue
    if res==1 and freq[-1]>0:
        print(0)
        continue
    if freq[-1]>0 and freq[1]==0:
        print(0)
        continue
    print(1)