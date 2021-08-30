"""UGLY NUMBER
Numbers having prime factors 2,3 or 5 only are called as ugly numbers.
So your Question is to write a function that will take an integer as input and
will check if that integer is an ugly number or not.

Ex :- in : 6 out : true Explain : 6 = 2 * 3
in : 14 out : false Explain : 14 = 7 * 2 so the prime factor is
7 along with 2 so it does not satisfy the requirements."""

def checkUgly(n):
    flag=True
    if(n==1):
        return flag
    if(n==0):
        return flag
    if(n%2==0):
        return checkUgly(n//2)
    elif(n%3==0):
        return checkUgly(n//3)
    elif(n%5==0):
        return checkUgly(n//5)
    else:
        flag = False
    return flag

n=int(input())
print(checkUgly(n))