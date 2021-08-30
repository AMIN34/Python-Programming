# cook your dish here
import math
def isPrime(n):
    c = 0
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

N = int(input())
c = 0
n = 2
while c != N:
    if isPrime(n) == True:
        c += 1
        print(n)
    n += 1