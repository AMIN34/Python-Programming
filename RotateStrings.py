import re
def leftrotate(s, d):
    tmp = s[d : ] + s[0 : d]
    return tmp
def rightrotate(s, d):
   return leftrotate(s, len(s) - d)

t=int(input())
while(t):
    s=list(input().split())
    k=int(input())
    y=[]
    for i in range(len(s)):
        y.append(rightrotate(s[i],k))
    res = len([key for key, val in enumerate(s) if val in set(y)])
    print(str(res))
    t-=1