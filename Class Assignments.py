'''#1)Write a Python Program to Find the Smallest Divisor of an Integer other than 1.
n=int(input("Enter integer: "))
for i in range(2,n+1):
    if(n%i==0):
        print("Smallest divisor: ",i)
        break
#2)Write a Python Program to Check whether a Number is a Palindrome or not.
n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")

#3)Write a Python Program to print the Prime Factors of an Integer.
n=int(input("Enter an integer:"))
print("Factors are:")
i=1
while(i<=n):
    k=0
    if(n%i==0):
        j=1
        while(j<=i):
            if(i%j==0):
                k=k+1
            j=j+1
        if(k==2):
            print(i)
    i=i+1

#4)Print the following pattern
rows = 8
for i in range(1, rows):
    for j in range(-1+i, -1, -1):
        print(format(2**j, "4d"), end=' ')
    print("")

#5)Print the following Pattern
for i in range(6):
    for j in range(6):
        if(i == 0 or i == 5 or j == 0 or j == 5):
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
    print()

#6)The set of input is given as ages. Then print the status according to the rules
print("Enter Age:- ")
age=int(input())
if(age>=0 and age<=1):
    print("In born")
elif(age>=2 and age<=10):
    print("Child")
elif(age>=11 and age<=17):
    print("young")
elif(age>=18 and age<=49):
    print("adult")
elif(age>=50 and age<=79):
    print("old")
else:
    print("very old")

#7)Convert a decimal number to a number of a given base b
def base10toN(num,n):
   return ((num == 0) and  "0" ) or ( base10toN(num // n, n).strip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[:n][num % n])
print("Enter Number:- ")
num=int(input())
print("Enter Base:- ")
b=int(input())
print(base10toN(num,b))
num=int(input("Enter Number:- "))
b=int(input("Enter Base:- "))
num=0
res=0
while(n!=0):
    rem=n%b
    num=num*10+rem
    n=n//b
while(num!=0):
    rem=num%10
    res=res*10+rem
    num=num//10
print("After conversion:- ",res)

#Class Assignment 2:-
#1)
list1 = [10, 20, 4, 45, 99]  
list1.sort() 
print("Largest element is:", list1[-1])


#2)
list1 = [10, 20, 4, 45, 99]  
list1.sort() 
print("Second Largest element is:", list1[-2])


#3)
list1 = [10, 20, 4, 45, 99]
el=[]
ol=[]
for i in range(len(list1)):
    if(list1[i]%2==0):
        el.append(list1[i])
    else:
        ol.append(list1[i])
print('Even list:-',el,'\n','Odd list:-',ol)


#4)
list1 = [10, 20, 4, 45, 99]
list2 = [9, 19, 3, 44, 91]
newlist=list1+list2
newlist.sort()
print(newlist)


#5)
a = [10, 20, 4, 45, 99]
for i in range(len(a)):
    for j in range((len(a)) - i - 1):
        if(a[j] > a[j + 1]):
             temp = a[j]
             a[j] = a[j + 1]
             a[j + 1] = temp
print('Second largest no. is',a[-2])


#6)
lst1 = [23, 15, 2, 14, 14, 16, 20 ,52] 
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
final_list = list(set().union(lst1, lst2))
print('Final union list:-',final_list)


#7)
lst1 = [23, 15, 2, 14, 14, 16, 20 ,52] 
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
print('Final intersection of two list:-',list(set(lst1) & set(lst2)))


#8)
low=int(input("Enter lower range: "))
upp=int(input("Enter upper range: "))
a=[]
a=[x for x in range(low,upp+1) if (int(x**0.5))**2==x and sum(list(map(int,str(x))))<10]
print(a)


#9)
a = [23, 15, 2, 14, 14, 16, 20 ,52]
b=[sum(a[0:x+1]) for x in range(0,len(a))]
print('The Cumulative Sum of a List where the ith Element is the Sum of the First i+1 Elements from The Original List:- ',b)


#10)
import random
a=[]
n=int(input('Enter number of elements:- '))
for _ in range(n):
    a.append(random.randint(1,20))
print('Randomised list is: ',a)
'''
# Class Assignment 3:-

#1) Write a Python program to unpack a tuple in several variables.
a= (10,11,50)
x,y,z = a  
print(x) 
print(y) 
print(z)

#2) Write a Python program to add an item in a tuple.
a= (10,11,13,43,50)
a=a+(9,)
print(a)
a=a[:3]+(12,41,45)
print(a)
a=list(a)
a.append(30)
a=tuple(a)
print(a)

#3) Write a Python program to convert a tuple to a string.
a=('a','m','i','n')
s=''.join(a)
print(s)

#4) Write a Python program to get the 4th element and 4th element from last of a tuple.
a=('a','m','i','n')+(10,11,13,43,50)
print(a[3])
print(a[-4])

#5) Write a Python program to find the repeated items of a tuple.
a=(10,11,13,43,50,10,11,13)
#for var in range(len(a)):
#    if(a.count(a[var])>1):
#        print(a[var])
a=list(a)
repeated = [] 
for i in range(len(a)): 
    for j in range(i+1,(len(a))): 
        if a[i] == a[j] and a[i] not in repeated: 
            repeated.append(a[i])
print(repeated)

#6) Write a Python program to check whether an element exists within a tuple.
a=('a','m','i','n')+(10,11,13,43,50)
print('m' in a)
print(6 in a)

#7) Write a Python program to convert a list to a tuple.
a=('a','m','i','n')+(10,11,13,43,50)
a=list(a)
print(a)

#8) Write a Python program to remove an item from a tuple.
a = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
a = a[:2] + a[3:]
print(a)
a = list(a) 
a.remove("Fri") 
a = tuple(a)
print(a)

#9) Write a Python program to find the length of a tuple.
a = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(len(a))

#10) Write a Python program to convert a tuple to a dictionary.
t=(('a', 30), ('b', 20), ('c', 10), ('e', 100))
print(dict((y,x) for x,y in t))

#11) Write a Python program to unzip a list of tuples into individual lists.
t=[(30, 'a'), (20, 'b'), (10, 'c'), (100, 'e')]
print(list(zip(*t)))

#12) Write a Python program to reverse a tuple.
a = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(tuple(reversed(a)))