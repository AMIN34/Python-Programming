start, end = [int(x) for x in input().split()]
l1=list()
for val in range(start, end + 1): 
    if val > 1:
        if val==2:
            l1.append(val)
        for n in range(2, val//2 + 2): 
            if (val % n) == 0: 
                break
            else: 
                if n == val//2 + 1: 
                    l1.append(val)
print(l1)
k=len(l1)
l2=list()
for i in range(0,k):
    for j in range (0,k):
        if(i!=j):
            m=l1[j]
            p=l1[i]*(10**(len(str(l1[j]))))
            l2.append(p+l1[j])
#print(l2)
l3=list()
for val in l2:
    val=int(val)
    if val > 1: 
        for n in range(2, val//2 + 2): 
            if (val % n) == 0: 
                break
            else: 
                if n == val//2 + 1: 
                    l3.append(val)
print(l3)
k=len(l3)
print(k)
ll=min(l3)
ul=max(l3)
print(ll,ul)
if k==1:
    print(ll)
else:
    for i in range(3,k+1):
        q=ll+ul
        ll=ul
        ul=q
print(ul)