""" def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)

t=int(input())
while(t):
    n=int(input())
    c=0
    for i in range(1,n):
        if(gcd(n,i)==1):
            c+=1
    print(c)
    t-=1 """

def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)

n=int(input())
c=0
for i in range(1,n):
    if(gcd(n,i)==1):
        c+=1
print(c)