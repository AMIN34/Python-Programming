def isprime(n1,n2):
    l1=list()
    for n in range(n1,n2+1):
        for i in range(2,n):
            if n%i==0:
                break
            else:
                l1.append(n)
    return l1
n1,n2=[int(x) for x in input().split()]
l1=isprime(n1,n2)
print(l1)