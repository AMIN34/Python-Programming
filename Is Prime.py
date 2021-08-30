def isprime(num):
    if (num%2==0):
        return False
    if num<2:
        return False
    i=2
    while(i*i<=num):
        if (num%i==0):
            return False
        i+=1
    return True
num=int(input())
print(isprime(num))