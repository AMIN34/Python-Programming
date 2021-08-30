'''#Assignment 1:-

# 1.Write a Python Program to Compute Simple Interest with all the required values.
p=float(input('Enter the principal amount(Rs.): '))
r=float(input('Enter the rate of interest(%): '))
t=float(input('Enter the time(yrs.): '))
print('Simple interest(Rs.): ',round( (p*r*t)/100,2) )


# 2.Write a Python Program to check whether a year is leap year or not.
year=int(input('\nEnter the year: '))
if (year%400==0):
    print('Its a leap year!!!')
elif (year%100==0):
    print('Its not a leap year!!!')
elif (year%4==0):
    print('Its a leap year!!!')
else:
    print('Its not a leap year!!!')


# 3.Write a Python Program to read height in centimeters and then Convert the Height to Feet and Inches.
height=float(input('\nEnter the height in centimeters(cm): '))
print('Height in feet(ft.): ',round(height*0.0328084,3))
print('Height in inches(in.): ',round(height*0.393701,3))


# 4.Write a Python Program to take the temperature in Celsius and convert it to the equivalent Fahrenheit.
celsius=float(input('\nEnter the temperature in degree celsius(°C): '))
print('Temperature in degree fahrenheit(°F): ',round((celsius*9/5)+32,2))


# 5.Write a Python code to display the biggest number among three inputted numbers using conditional statements.
num1=float(input('\nEnter first number: '))
num2=float(input('Enter second number: '))
num3=float(input('Enter third number: '))

if(num1==num2 and num2==num3):
    print('All numbers are equal!!!')
else:
    if(num2>num1 and num2>num3):
        print('Biggest number: ',num2)
    elif(num3>num1 and num3>num2):
        print('Biggest number: ',num3)
    else:
        print('Biggest number: ',num1)


#Assignment 2:-

#1)Write a Python Program to Find the Largest Number in a List.
list1 = [10, 20, 4, 45, 99]  
list1.sort() 
print('Largest element is:', list1[-1])


#2)Write a Python Program to Find the Second Largest Number in a List.
list1 = [10, 20, 4, 45, 99]  
list1.sort() 
print('Second Largest element is:', list1[-2])


#3)Write a Python Program to Put Even and Odd elements of a List into Two Different Lists.
list1 = [10, 20, 4, 45, 99]
el=[]
ol=[]
for i in range(len(list1)):
    if(list1[i]%2==0):
        el.append(list1[i])
    else:
        ol.append(list1[i])
print('Even list:-',el,'\n','Odd list:-',ol)


#4)Write a Python Program to Merge Two Lists and Sort it.
list1 = [10, 20, 4, 45, 99]
list2 = [9, 19, 3, 44, 91]
newlist=list1+list2
newlist.sort()
print('New list:-',newlist)


#5)Write a Python Program to Find the Second Largest Number in a List Using Bubble Sort.
a = [10, 20, 4, 45, 99]
for i in range(len(a)):
    for j in range((len(a)) - i - 1):
        if(a[j] > a[j + 1]):
             temp = a[j]
             a[j] = a[j + 1]
             a[j + 1] = temp
print('Second largest no. is',a[-2])


#6)Write a Python Program to Find the Union of two Lists.
lst1 = [23, 15, 2, 14, 14, 16, 20 ,52] 
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
final_list = list(set().union(lst1, lst2))
print('Final union list:-',final_list)


#7)Write a Python Program to Find the Intersection of Two Lists.
lst1 = [23, 15, 2, 14, 14, 16, 20 ,52] 
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
print('Final intersection of two list:-',list(set(lst1) & set(lst2)))


#8)Write a Python Program to Find all Numbers in a Range which are Perfect Squares and Sum of all Digits in the Number is Less than 10.
low=int(input('Enter lower range: '))
upp=int(input('Enter upper range: '))
a=[]
a=[x for x in range(low,upp+1) if (int(x**0.5))**2==x and sum(list(map(int,str(x))))<10]
print('All Numbers in range (',low,',',upp,'_which are Perfect Squares and Sum of all Digits in the Number is Less than 10.:-',a)


#9)Write a Python Program to Find the Cumulative Sum of a List where the ith Element is the Sum of the First i+1 Elements from The Original List.
a = [23, 15, 2, 14, 14, 16, 20 ,52]
b=[sum(a[0:x+1]) for x in range(0,len(a))]
print('The Cumulative Sum of a List where the ith Element is the Sum of the First i+1 Elements from The Original List:- ',b)


#10)Write a Python Program to Generate Random Numbers from 1 to 20 and Append Them to the List.
import random
a=[]
n=int(input('Enter number of elements:- '))
for _ in range(n):
    a.append(random.randint(1,20))
print('Randomised list is: ',a)


#Assignment 3:-

#1) Write a Python program to unpack a tuple in several variables.
a=(10,11,50)
print('Given tuple:- ',a)
x,y,z = a  
print('After unpacking the tuple we get:-',x,y,z,end='') 


#2) Write a Python program to add an item in a tuple.
a= (10,11,13,43,50)
print('Given tuple:- ',a)
a=a+(9,)
print('Adding element by using '+':-',a)
a=a[:3]+(12,41,45)
print('Adding element by using slicing',a)
a=list(a)
a.append(30)
a=tuple(a)
print('Adding element with the help of list',a)


#3) Write a Python program to convert a tuple to a string.
a=('a','m','i','n')
print('Given tuple:- ',a)
s=''.join(a)
print('After converting to string',s)


#4) Write a Python program to get the 4th element and 4th element from last of a tuple.
a=('a','m','i','n')+(10,11,13,43,50)
print('Given tuple:- ',a)
print('The 4th element',a[3])
print('4th element from last',a[-4])


#5) Write a Python program to find the repeated items of a tuple.
a=(10,11,13,43,50,10,11,13)
print('Given tuple:- ',a)
a=list(a)
repeated = [] 
for i in range(len(a)): 
    for j in range(i+1,(len(a))): 
        if a[i] == a[j] and a[i] not in repeated: 
            repeated.append(a[i])
print('Hence the repeated the elements are:-',repeated)


#6) Write a Python program to check whether an element exists within a tuple.
a=('a','m','i','n')+(10,11,13,43,50)
print('Given tuple:- ',a)
x=input('Enter element to search:- ')
if(x in a):
    print('Exist')
else:
    print('Does not exist')


#7) Write a Python program to convert a list to a tuple.
a=['yonder', 'window', 'breaks', 'light', 'what','soft', 'but', 'in']
print('Original list:-',a)
a=tuple(a)
print('After converting List to tuple:-',a)


#8) Write a Python program to remove an item from a tuple.
a = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print('Given tuple:- ',a)
print('Removing 3rd index element using slicing')
a = a[:2] + a[3:]
print('Fnal Tuple:- ',a)
print('Removing element with the help of list')
a = list(a) 
a.remove('Fri') 
a = tuple(a)
print('Final Tuple',a)


#9) Write a Python program to find the length of a tuple.
a = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print('Hence the length of the tuple is:- ',len(a))


#10) Write a Python program to convert a tuple to a dictionary.
t=(('a', 30), ('b', 20), ('c', 10), ('e', 100))
print('Changing a tuple to dictionary we get:- ',end='')
print(dict((y,x) for x,y in t))


#11) Write a Python program to unzip a list of tuples into individual lists.
t=[(30, 'a'), (20, 'b'), (10, 'c'), (100, 'e')]
print('Unzip a list of tuples into individual lists, we get:- ',end='')
print(list(zip(*t)))


#12) Write a Python program to reverse a tuple.
a = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print('After reversing the tuple we get',tuple(reversed(a)))


# Assignment 4

# 1)Write a Python function to find the Max of three numbers.
def maximum(a, b, c): 
    if (a >= b) and (a >= c): 
        largest = a 
    elif (b >= a) and (b >= c): 
        largest = b 
    else: 
        largest = c 
    return largest
a,b,c=[int(x) for x in input('Enter three values: ').split()]
print('Largest no.:-',maximum(a,b,c),'\n')
def max_of_two( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
a,b,c=[int(x) for x in input('Enter three values: ').split()]
print('Largest no.:-',max_of_three(a,b,c),'\n')



# 2)Write a Python function to sum all the numbers in a list.
def total(numbers):
    t = 0
    for x in numbers:
        t += x
    return t
print(total((8, 2, 3, 0, 7)),'\n')

# 3)Write a Python function to multiply all the numbers in a list.
def multiply(numbers):  
    t = 1
    for x in numbers:
        t *= x  
    return t  
print(multiply((8, 2, 3, -1, 7)),'\n')

# 4)Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input('Input number to calculate the factiorial : '))
print(factorial(n))

# 5)Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
def string_test(s):
    d={'u':0, 'l':0}
    for c in s:
        if c.isupper():
           d['u']+=1
        elif c.islower():
           d['l']+=1
        else:
           pass
    print ('Original String : ', s)
    print ('No. of Upper case characters : ', d['u'])
    print ('No. of Lower case Characters : ', d['l'])
string_test('The quick Brown Fox')

# 6)Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x
print(unique([1,2,3,3,3,3,4,5]))

# 7)Write a Python function to check whether a number is perfect or not.
def perfectnum(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
n=int(input('Enter no.:- '))
print(perfectnum(n))

# 8)Write a Python function that checks whether a passed string is palindrome or not.
def ispalindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return ispalindrome(s[1:-1])
        else:
            return False
a=str(input("Enter string:"))
if(ispalindrome(a)==True):
    print("String is a palindrome")
else:
    print("String isn't a palindrome")

# 9)Write a Python function to check whether a string is a pangram or not.
import string
def pangram(string, alphabets):
    for char in alphabets:
        if char not in string.lower():
            return False
    return True
str1=input("Enter string:- ")
alphabets = string.ascii_lowercase
print('\n',pangram(str1,alphabets))

# 10)Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
print('Enter a hyphen separated sequence of words:- ')
lst=[n for n in input().split('-')]  
lst.sort()
print("Sorted:")
print('-'.join(lst))

# 11)Write a python program to show the permutation and combination of a inputted List.
import itertools
seq = itertools.permutations(['a','b','c'])
for p in list(seq):
   print(p)
combi = itertools.combinations(['p', 'y', 't', 'h', 'o', 'n'], 5)
for c in list(combi):
   print(c)
   

# Assignment 4.1

# 1) pattern 1
def pattern1(n):
    for i in range(1, n):
        for j in range(-1+i, -1, -1):
            print(format(2**j, "4d"), end=' ')
        print()
n=int(input('Enter no. of rows:- '))
pattern1(n)

# 2) pattern 2
def pattern2(n):
    for i in range(n):
        num=10
        for j in range(i+1):
            print(num, end=" ")
            num = num-2
        print()
n=int(input('Enter no. of rows:- '))
pattern2(n)

#3) pattern 3
def pattern3(n):
    for i in range(n+1):
        for j in range(1,i+1):
            print(j, end=' ')
        for j in range(i+1, 0, -1):
            print(j, end=' ')
        print()
n=int(input('Enter no. of rows:- '))
pattern3(n)

#4) pattern 4
def pattern4(n):
    for i in range(n+1):
        for j in range(n-i,0,-1):
            print(j,' ',end='')
        print()
n=int(input('Enter no. of rows:- '))
pattern4(n)

# 5) pattern 5
def pattern5(n):
    for i in range(n):
        for j in range(i + 1):
            print(i * j, end='  ')
        print()
n=int(input('Enter no. of rows:- '))
pattern5(n)


#6) pattern 6
def pattern6(n):
    for i in range(n):
        for j in range(n - 1, i, -1):
            print(j, '', end='')
        for l in range(i):
            print('    ', end='')
        for k in range(i + 1, n):
            print(k, '', end='')
        print('\n')
n=int(input('Enter no. of rows:- '))
pattern6(n)


#Assignment 5

# 1) Write a Python program to create a set
x=set() #Creating an empty set
print('A empty set ',x)
n=set([0,1,2,3,4]) #creating a non empty set
print('A non-empty set ',n)
print()

# 2) Write a Python program to iterate over a sets
n=set([0,1,2,3,4])
print('Given set - ',n)
print('Printing elements --')
for i in n:
	print(i)
print()

# 3) Write a Python program to add member(s) in set
x=set()
print('Adding a new element in the ',x)
x.add('Bottle')
print('Current set- ',x)
print('Updating set')
x.update(['Water','Colour'])
print('New set',x)
print()

# 4) Write a Python program to remove item(s) from set
n=set([0,1,2,3,4])
print('Original set - ',n)
n.pop()
print('After using pop function once- ',n)
print()

# 5) Write a Python program to remove an item if it is present in the set
n=set([0,1,2,3,4])
print('Original set -',n)
print('Discrding 4')
n.discard(4)
print(n)
print()

# 6) Write a Python program to create a union & intersection of sets
n=set([0,1,2,3,4])
print('Set 1:- ',n)
n1=set([2,3,5,6,7,9])
print('Set 2:- ',n1)
print('Union of the sets:- ',n|n1)
print('Intersection of the sets:- ',n & n1) 
print()

# 7) Write a Python program to create set difference & symmetric difference
n=set([0,1,2,3,4])
print('Set A:- ',n)
n1=set([2,3,5,6,7,9])
print('Set B:- ',n1)
print('Set difference between (A & B) and (B & A) is--',n-n1,'and',n1-n,'respectively' )
print('Symmetric difference between A & B is--',n^n1 )
print()

# 8) Write a Python program to check if a set is a subset of another set
n=set([0,1,2,3,4])
print('Set A:- ',n)
n1=set([2,3,5,6,7,9])
print('Set B:- ',n1)
n2={2,3}
print('Set C:- ',n2)
print('Is set A is a subset of set B? ')
print(n.issubset(n1))
print('Is set B is a subset of set A? ')
print(n1.issubset(n))
print('Is set C is a subset of set A? ')
print(n2.issubset(n))
print('Is set C is a subset of set B? ')
print(n2.issubset(n1))
print()
# 9) Write a Python program to calculate the length and then clear the set
n=set([1,2,3,5,6,7,9])
print('Given set - ',n)
print('The length of the set is ',len(n))
print('Clearing set')
n.clear()
print('Current set:- ',n) 
print()

# 10) Write a Python program to find the maximum and minimum value in a set
n=set([1,2,3,5,6,7,9])
print('Given set - ',n)
print('Maximum value in the set -',max(n))
print('Minimum value in the set -',min(n))
print()

# 11) Write a Python program to find the length of a set
n=set([1,2,3,5,6,7,9])
print('Given set - ',n)
print('The length of the set is ',len(n))
print()

# 12) Write a Python program to to check if a given value is present or not
n = {1, 3, 5, 7, 9, 11}
print("Original set:- ",n)
print("Testing if 6 exists in n:")
print(6 in n)
print("Testing if 7 exists in n:")
print(7 in n)
print("Testing if 11 exists in n:")
print(11 in n)
print("Testing if 0 exists in n:")
print(0 in n)
print("\nTesting if 6 is not in n")
print(6 not in n)
print("Testing if 7 is not in n")
print(7 not in n)
print("Testing if 11 is not in n")
print(11 not in n)
print("Testing if 0 is not in n")
print(0 not in n)
print()

#13) Write a Python program to check if a set is superset of itself and superset of another given set
n=set([0,1,2,3,4])
print('Set A:- ',n)
n1=set([2,3,5,6,7,9])
print('Set B:- ',n1)
n2={2,3}
print('Set C:- ',n2)
print('Testing if set A is superset of itself')
print(n.issuperset(n))
print('Testing if set A is superset of set B')
print(n.issuperset(n1))
print('Testing if set A is superset of set C')
print(n.issuperset(n2))
print()

# 14) Write a Python program to remove the intersection of a 2nd set from the first set
n=set([0,1,2,3,4])
print('Set A:- ',n)
n1=set([2,3,5,6,7,9])
print('Set B:- ',n1)
print("Removing the intersection of a 2nd set from the 1st set using difference_update():")
n.difference_update(n1)
print(n)
n=set([0,1,2,3,4])
print('Set A:- ',n)
n1=set([2,3,5,6,7,9])
print('Set B:- ',n1)
print("Removing the intersection of a 2nd set from the 1st set using -= operator:")
print(n-n1)
print()

# Assignment 6

# 1) Write a Python program to create an 3X3 with Random values and print the matrix
import numpy as np
x=np.random.randint(1,50,size=(3,3))
print(x)
print()

# 2) Write a Python program to create an 3X3 Matrix and calculate sum of the diagonal elements
import numpy as np
x=np.random.randint(1,50,size=(3,3))
print(x)
print('Sum of the diagonal elements is:- ')
print(np.trace(x))
print()

# 3) Write a Python program to perform the addition of two 3X3 Matrices
import numpy as np
X=np.random.randint(1,50,size=(3,3))
print(X)
Y=np.random.randint(1,50,size=(3,3))
print(Y)
result = [[X[i][j] + Y[i][j]  for j in range(len(X[0]))] for i in range(len(X))]
for r in result:
   print(r)
print()
   
# 4) Write a Python program to perform the elements-wise multiplication of two 3X3 Matices
import random
import numpy as np
a = np.random.randint(10, 99, size=(3, 3))
b = np.random.randint(0, 10, size=(3, 3))
print('Your matrices are: \n', a, end='')
print('\nand \n', b)
print('The multiplication of the two matrices: \n', np.multiply(a, b))
print()

# 5. Write a python program to perform the Matrix Multiplication of two 3X3 Matrixes.
import random
import numpy as np
a = np.random.randint(10, 99, size=(3, 3))
b = np.random.randint(0, 10, size=(3, 3))
print('Your matrices are: \n', a, end='')
print('\nand \n', b)
print('The multiplication of the two matrices: \n', np.matmul(a, b))
print()

# 6. Write a python program to find the rank of a matrix.
import random
import numpy as np
a = np.random.randint(10, 99, size=(7, 5))
print('The matrix: \n', a)
print('The rank of the matrix is: ', np.linalg.matrix_rank(a))
print()

# 7. Write a python program to find the trace of a matrix.
import random
import numpy as np
a = np.random.randint(10, 99, size=(4, 4))
print('The matrix: \n', a)
print('The trace of the matrix is: ', a.diagonal().sum())
print()

# 8. Write a python program to find the determinant of a matrix.
import random
import numpy as np
a = np.random.randint(1, 10, size=(3, 3))
print('The matrix: \n', a)
det = np.linalg.det(a)
print('The determinant of the matrix is: ', round(det, 2))
print()

# 9. Write a python program to solve a set of linear equations.

import numpy as np
# Solve the following systems of linear equations by Gaussian elimination method:
# question 1
# 5x - 3y = 0
# 16x + 4y = -4
a = np.array([[5, -3], [16, 4]])
b = np.array([0, -4])
s = np.linalg.solve(a, b)
print(s)
# question 2
# 2x − 2y + 3z = 2
# x + 2y − z = 3
# 3x − y + 2z = 1
a = np.array([[2, -2, 3], [1, 2, -1], [3, -1, 2]])
b = np.array([2, 3, 1])
s = np.linalg.solve(a, b)
print(s)
print()

# 10.Write a python program to find mean, median, and mode of a set of elements.
import random
import numpy as np
a = np.random.randint(1, 999, size=(1, 10))
print('Given set: ', a)
print('Mean: ', np.mean(a))
print('Median: ', np.median(a))
#The mode() method returns a ModeResult object that contains the mode number , and count (how many times the mode number appeared.
from scipy import stats
x = stats.mode(a)
print('Mode: ', x)
print()

# 11.Write a python program to find row wise maximum and column wise minimum element.
import random
import numpy as np
a = np.random.randint(1, 999, size=(6, 4))
print('The matrix: \n', a)
print('Column wise minium elements: ', np.min(a, axis=0))
print('Row wise maximum elements: ', np.max(a, axis=1))
print()

# 12.Write a python program to find the subtraction of individual elements of two array.
import random
import numpy as np
a = np.random.randint(10, 99, size=(3, 3))
b = np.random.randint(0, 10, size=(3, 3))
print('Your matrices are: \n', a, end='')
print('\nand \n', b)
print('Subtraction of two array is: \n', a-b)
print()


#Assignment6(linear equation)

"""1.
4x-2y=2
x-y=0"""

#using sympy
from sympy import symbol,Eq,solve
x,y=symbols('x y')
equation1=Eq(4*x-2*y-2)
equation2=Eq(x-y)
solution=solve((equation1,equation2),(x,y))
print(solution)

#using linalg
import numpy as np
a=np.array([[4,-2],[1,-1]],dtype=int)
b=np.array([2,0],dtype=int)
result=np.linalg.solve(a,b)  #this is the library function to solve two linear equation
print(np.array(result))
#{x: 1, y: 1}
#[1. 1.]

"""2.
A+B+C=10
2A+B-C=5
3A+3B+4C=36"""

#using sympy
from sympy import symbol,Eq,solve
a,b,c=symbols('A B C')
equation1=Eq(a+b+c-10)
equation2=Eq(2*a+b-c-5)
equation3=Eq(3*a+3*b+4*c-36)
solution=solve((equation1,equation2,equation3),(a,b,c))
print(solution)

#using linalg
import numpy as np
a=np.array([[1,1,1],[2,1,-1],[3,3,4]],dtype=int)
b=np.array([10,5,36],dtype=int)
result=np.linalg.solve(a,b)  #this is the library function to solve two linear equation
print(np.array(result))
#ans:{A: 7, B: -3, C: 6}
#[ 7. -3.  6.]

"""3.
-3x + 2y -5z = -14
2x - 3y +4z = 10
x + y + z = 4"""

#using sympy
from sympy import symbol,Eq,solve
x,y,z=symbols('x y z')
equation1=Eq(-3*x+2*y-5*z+14)
equation2=Eq(2*x-3*y+4*z-10)
equation3=Eq(x+y+z-4)
solution=solve((equation1,equation2,equation3),[x,y,z])
print(solution)

#using linalg
import numpy as np
a=np.array([[-3,2,-5],[2,-3,4],[1,1,1]],dtype=int)
b=np.array([-14,10,4],dtype=int)
result=np.linalg.solve(a,b)  #this is the library function to solve two linear equation
print(np.array(result))
#ans:{y: 2*z/5 - 2/5, x: 22/5 - 7*z/5}
#[-2.6  1.6  5. ]

"""4.
x+2y−z=4
2x+y+z=−2
x+2y+z=2"""

#using sympy
from sympy import symbol,Eq,solve
x,y,z=symbols('x y z')
equation1=Eq(x+2*y-z-4)
equation2=Eq(2*x+y+z+2)
equation3=Eq(x+2*y+z-2)
solution=solve((equation1,equation2,equation3),[x,y,z])
print(solution)

#using linalg
import numpy as np
a=np.array([[1,2,-1],[2,1,1],[1,2,1]],dtype=int)
b=np.array([4,-2,2],dtype=int)
result=np.linalg.solve(a,b)  #this is the library function to solve two linear equation
print(np.array(result))
#ans: {x: -5/3, y: 7/3, z: -1}
#[-1.66666667  2.33333333 -1. ]


#Assignment 7

#1. Write a Python program to calculate the length of a string.

#with library function
mystr=input("Enter a string:")
print("The length of your string is:",len(mystr))

#without library function
mystr=input("Enter a string:")
count=0
for letter in mystr:
    count=count+1
print("The length of your string is:",count)


#2. Write a Python program to count the number of characters (character frequency) in a string.
#Sample String : google.com'
#Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}"""


#with library function
mystr=input("Enter a string:")
mydict={}
for letter in mystr:
    mydict[letter]=mydict.get(letter,0)+1  #if letter is found in dict then return its value or return 0
print("The number of characters in a string is:")
print(mydict)

#without library function
mystr=input("Enter a string:")  
mydict={}
for letter in mystr:
    if letter in mydict.keys():
        mydict[letter]=mydict[letter]+1
    else:
        mydict[letter]=1
print("The number of characters in a string is:")
print(mydict)


#3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
#Sample String : 'w3resource'
#Expected Result : 'w3ce'
#Sample String : 'w3'
#Expected Result : 'w3w3'
#Sample String : ' w'
#Expected Result : Empty String"""


#with library function
mystr=input("Enter a string:")  #here we will put input strings 'w3resource','w3','w'
new_str=""
if len(mystr)<2:
    new_str="Empty String"
elif len(mystr)==2:
    new_str=mystr+mystr
else:
    new_str=mystr[:2]+mystr[-2:]
print("New string is:",new_str)

#without library function
mystr=input("Enter a string:")
new_str=""
count=0
for letter in mystr:
    count=count+1
if count<2:
    new_str="Empty String"
elif count==2:
    new_str=mystr+mystr
else:
    new_str=mystr[:2]+mystr[-2:]
print("New string is:",new_str)


#4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
#Sample String : 'restart'
#Expected Result : 'resta$t'"""

#with library function
mystr=input("Enter a string:")
first=mystr[0]
mystr=first+mystr[1:].replace(first,"$")
print("New string is:",mystr)

#without library function
mystr=input("Enter a string:")   
first=mystr[0]
new_str=first
for letter in mystr[1:]:
    if letter==first or letter==first.lower():
        new_str=new_str+"$"
    else:
        new_str=new_str+letter
print("New string is:",new_str)


#5. Write a Python program to add 'ing' at the end of a given string (length should be at
least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string
length of the given string is less than 3, leave it unchanged.
#Sample String : 'abc'
#Expected Result : 'abcing'
#Sample String : 'string'
#Expected Result : 'stringl

#without library function
mystr=input("Enter a string:")   
new_str=""
if len(mystr)<3:
    new_str=mystr
elif mystr[-3:]=="ing":
    new_str=mystr+"ly"
else:
    new_str=mystr+"ing"
print("The new string is:",new_str)


#6. Write a Python function that takes a list of words and returns the length of the longest one.

#with library function
ylist=input("Enter multiple words seperated by space").split()
mylist=sorted(mylist,key=len,reverse=True)
print(mylist)
print("The length of longest word is:",len(mylist[0]))

#without library function
mylist=input("Enter multiple words seperated by space").split()
longest_count=0
for words in mylist:
    count=0
    for letter in words:
        count=count+1
    if count>longest_count:
        longest_count=count
print("The length of longest word is:",longest_count)


#7. Write a Python program to remove the characters which have odd index values of a given string.

#without library function
mystr=input("Enter a string:")
count=0
new_str=""
for letter in mystr:
    count=count+1
    if(count%2==0):  #even position
        new_str=new_str+letter
print("The string after removing new_strthe characters which have odd index values is:")
print(new_str)


#8. Write a Python program to count the occurrences of each word in a given sentence.

#with library function
mylist=input("Enter a string:").split()
mydict={}
for words in mylist:
    mydict[words]=mydict.get(words,0)+1  #if letter is found in dict them return its value or return 0
print("The occurances of words in a string is:")
print(mydict)

#without library function
mylist=input("Enter a string:").split()
mydict={}
for word in mylist:
    if word in mydict.keys():
        mydict[word]=mydict[word]+1
    else:
        mydict[word]=1
print("The occurances of words in a string is:")
print(mydict)


#9. Write a Python script that takes input from the user and displays that input back in upper and lower cases.

#with library function
mystr=input("Enter a string:")
print("The string in upper case is:",mystr.upper())
print("The string in lower case is:",mystr.lower())

#without library function
mystr=input("Enter a string:")
upper_str=""
lower_str=""
for letter in mystr:
    if ord(letter)>=97 and ord(letter)<=122:
        upper_str=upper_str+chr(ord(letter)-32)
    else:       
        upper_str=upper_str+letter

for letter in mystr:
    if ord(letter)>=65 and ord(letter)<=90:
        lower_str=lower_str+chr(ord(letter)+32)
    else:       
        lower_str=lower_str+letter

print("The string in upper case is:",upper_str)
print("The string in lower case is:",lower_str)


#10. Right a Python script to reverse a string.

#without library function
mystr=input("Enter a string:")
print("Reversed string is:",mystr[-1::-1])


# Assignment 8

# 1. Write a Python script to sort (ascending and descending) a dictionary by value.
import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',d)
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)

# 2. Write a Python script to add a key to a dictionary.
d = {0:10, 1:20}
print(d)
d.update({2:30})
print(d)

# 3. Write a Python script to concatenate following dictionaries to create a new one.
#Sample Dictionary :
#dic1={1:10, 2:20}
#dic2={3:30, 4:40}
#dic3={5:50,6:60}
#Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)

# 4. Write a Python script to check whether a given key already exists in a dictionary.
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)

# 5. Write a Python program to iterate over dictionaries using for loops.
d = {'x': 10, 'y': 20, 'z': 30} 
for dict_key, dict_value in d.items():
    print(dict_key,'->',dict_value)

# 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
n=int(input("Input a number "))
d = dict()
for x in range(1,n+1):
    d[x]=x*x
print(d)

# 7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys. 
d=dict()
for x in range(1,16):
    d[x]=x**2
print(d)

# 8. Write a Python script to merge two Python dictionaries.
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)
print(d)

# 9. Write a Python program to sum all the items in a dictionary.
my_dict = {'data1':100,'data2':-54,'data3':247}
print(sum(my_dict.values()))

# 10. Write a Python program to get a dictionary from an object's fields.
class dictObj(object):
     def __init__(self):
         self.x = 'red'
         self.y = 'Yellow'
         self.z = 'Green'
     def do_nothing(self):
         pass
test = dictObj()
print(test.__dict__)

# 11. Write a Python program to multiply all the items in a dictionary.
my_dict = {'data1':100,'data2':-54,'data3':247}
result=1
for key in my_dict:    
    result=result * my_dict[key]
print(result)

# 12. Write a Python program to remove a key from a dictionary.
myDict = {'a':1,'b':2,'c':3,'d':4}
print(myDict)
if 'a' in myDict: 
    del myDict['a']
print(myDict)

# 13. Write a Python program to map two lists into a dictionary.
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
color_dictionary = dict(zip(keys, values))
print(color_dictionary)

# 14. Write a Python program to sort a dictionary by key.
colordict = {'r':'F','g':'08','b':'00','w':'FF'}
for key in sorted(colordict):
    print("%s: %s" % (key, colordict[key]))

# 15. Write a Python program to get the maximum and minimum value in a dictionary.
my_dict = {'x':500, 'y':5874, 'z': 560}
key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))
print('Maximum Value: ',my_dict[key_max])
print('Minimum Value: ',my_dict[key_min])


# Assignment 8.1

# 1) Write a Python program to remove duplicates (Value) from Dictionary.
stddict={'1':'a','2':'a','3':'c','4':'d',}
res={}
for key,value in stddict.items():
    if value not in res.values():
        res[key]=value
print(res)

def dup(dic):
    d = {}
    k = 1
    for i in dic.values():
        if i not in d.values():
            d.update({k : i})
            k += 1
    return d
print("Before removing duplicates : ", stddict)
new_dic = dup(stddict)
print("After removing duplicates : ", new_dic)


# 2) Write a Python program to check a dictionary is empty or not.
d={}
if not bool(d):
    print("Dictionary is empty")

dict1 = {1: "Jan", 2: "Feb", 3: "March", 4: "aprin", 5: "may"}
dict2 = {'a': 400, 'b': 400, 'd': 400, 'c': 300}
dict3 = {}
dict4 = {1: 'A', 2: 'B', 3: 123, 4: 123, 5: 'C', 6: 'B'}
dict5 = {"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}
dict6 = {1: "Hello", 2: 7, 3: "Hi", 4: 45.60, 5: "January", 6: 43, 7: "Dictionary", 8: "Hi", 9: 7}

lst = [dict1, dict2, dict3, dict4, dict5, dict6]

for i in range(0, len(lst)):
    if len(lst[i]) == 0:
        print("dict", i+1, " is an empty dictionary")
    else:
        print("dict", i+1, " is not empty")


# 3) Write a Python program to combine two dictionary adding values for common keys.
#d1 = {'a': 100, 'b': 200, 'c':300}
#d2 = {'a': 300, 'b': 200, 'd':400}
#Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = Counter(d1) + Counter(d2)
print(d)

"""Without using counter"""
d = dict()
for i in d1.keys() & d2.keys():
    k = i
    v = d1.get(k) + d2.get(k)
    d.update({k : v})

for i in d1.keys():
    if i not in d.keys():
        d.update({i : d1.get(i)})

for i in d2.keys():
    if i not in d.keys():
        d.update({i: d2.get(i)})

print("\tWithout counter: ", "\tUpdated dictionary : ", d)


# 4) Write a Python program to print all unique values in a dictionary.
"""Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}"""

d = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print("Original List: ",d)
v= set( val for dic in d for val in dic.values())
print("Unique Values: ",v)


# 5) Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
"""Sample data : {'1':['a','b'], '2':['c','d']}
Expected Output:
ac
ad
bc
bd"""

from itertools import product
d ={'1':['a','b'], '2':['c','d']}
for x, y in product(*d.values()):
    print(x + y)


# 6. Write a Python program to find the highest 3 values in a dictionary.
def findmax(dc, n):
    lst = list(dc.values())
    mxlst = []
    for i in range(n):
        x = max(lst)
        mxlst.append(x)
        lst = [i for i in lst if i != x]
    return mxlst

dic_1 = {'a': 900, 'b': 460, 'd': 400, 'c': 300}
dic_2 = {'A':  2, 'B': 3, 'C': 4, 'D': 123, 'E': 5,  'F': 6}
d1 = findmax(dic_1, 3)
d2 = findmax(dic_2, 3)
print("3 highest values of dictionary 1: ", d1)
print("3 highest values of dictionary 2: ", d2)


# 7. Write a Python program to combine values in python list of dictionaries.
#
#   Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
#   Expected Output: Counter({'item1': 1150, 'item2': 300})
from collections import Counter
lst = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
result = Counter()
for d in lst:
    result[d['item']] += d['amount']
print("\t Input: ", lst, "\n", "\tOutput: ", result)


# 8. Write a Python program to convert a list into a nested dictionary of keys.
numlist = [1, 2, 3, 4, 5, 6, 7]
newdict = current = {}
for name in numlist:
    current[name] = {}
    current = current[name]
print(newdict)


# 9. Write a Python program to sort a list alphabetically in a dictionary.
dic = {'n1': [2, 3, 1, 16], 'n2': [5, 1, 2], 'n3': [3, 2, 8, 15, 22, 4]}
print("Before: ", dic)
for i in dic:
    key = i
    lst = dic.get(i)
    lst = sorted(lst)
    dic.update({key : lst})
print("After: ", dic)


# 10.Write a Python program to count number of items in a dictionary value that is a list.
dic = {'A': ['subj1', 'subj2', 'subj3'], 'S': ['subj1', 'subj2'], 1: ['Jan', 'Feb'], 2: ['March', 'april', 'may']}
sum = 0
for d in list(dic.values()):
    sum += len(d)
print("\tDictionary: ", dic, "\n", "\tThe total length is: ", sum)
'''
"""
# Assignment 9

#1)
import matplotlib.pyplot as plt  
import numpy as np  
x=np.array([0,50])
y=np.array([0,50])
plt.plot(x,y)  
plt.title('Draw a line')  
plt.show()

#2)
import matplotlib.pyplot as plt  
import numpy as np 
x=np.array([1,2,3])
y=np.array([2,4,0])
plt.plot(x,y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Sample graph!')  
plt.show()


#3)
import matplotlib.pyplot as plt  
import numpy as np 
x=np.array([1,2,3])
y=np.array([2,4,1])
plt.plot(x,y)  
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Sample graph!')  
plt.show()


#4) Write a Python program to draw line charts of the financial data of Alphabet Inc. between October 3, 2016 to October 7, 2016. 
# Sample Financial data (fdata.csv):
'''Date,Open,High,Low,Close
10-03-16,774.25,776.065002,769.5,772.559998
10-04-16,776.030029,778.710022,772.890015,776.429993
10-05-16,779.309998,782.070007,775.650024,776.469971
10-06-16,779,780.47998,775.539978,776.859985
10-07-16,779.659973,779.659973,770.75,775.080017'''

'''import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('fdata.csv', sep=',', parse_dates=True, index_col=0)
df.plot()
plt.show()'''

import matplotlib.pyplot as plt
x=['10-03-16','10-04-16','10-05-16','10-06-16','10-07-16']
y1= [774.25, 776.030029, 779.309998, 779, 779.659973]
y2= [776.065002, 778.710022, 782.070007, 780.47998, 779.659973]
y3= [769.5, 772.890015, 775.650024, 775.539978, 770.75]
y4= [772.559998, 776.429993, 776.469971, 776.859985, 775.080017]
plt.xlabel('Date')
plt.ylabel('Data')
plt.title('Financial Data')
plt.plot(x,y1, color='blue', label = 'open')
plt.plot(x,y2, color='orange', label = 'high')
plt.plot(x,y3, color='green', label = 'low')
plt.plot(x,y4, color='red', label = 'close')
plt.legend()
plt.show()


#5) Write a Python program to plot two or more lines on same plot with suitable legends of each line.
import matplotlib.pyplot as plt
# line 1 points
x1 = [10,20,30]
y1 = [20,40,10]
plt.plot(x1, y1, label = "line 1")

# line 2 points
x2 = [10,20,30]
y2 = [40,10,30]
plt.plot(x2, y2, label = "line 2")

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Two or more lines on same plot with suitable legends ')
# show a legend on the plot
plt.legend()
plt.show()


#6) Write a Python program to plot two or more lines with legends, different widths and colors.
import matplotlib.pyplot as plt
# line 1 points
x1 = [10,20,30]
y1 = [20,40,10]
#plt.plot(x1, y1, label = "line 1")

# line 2 points
x2 = [10,20,30]
y2 = [40,10,30]
#plt.plot(x2, y2, label = "line 2")

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Two or more lines on same plot with suitable legends ')
plt.plot(x1,y1, color='blue', linewidth = 3,  label = 'line1-width-3')
plt.plot(x2,y2, color='red', linewidth = 5,  label = 'line2-width-5')
# show a legend on the plot
plt.legend()
plt.show()


#7) Write a Python program to plot two or more lines with different styles.
import matplotlib.pyplot as plt
# line 1 points
x1 = [10,20,30]
y1 = [20,40,10]
#plt.plot(x1, y1, label = "line 1")

# line 2 points
x2 = [10,20,30]
y2 = [40,10,30]
#plt.plot(x2, y2, label = "line 2")

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('plot two or more lines with different styles.')
plt.plot(x1,y1, color='blue', linewidth = 3,  label = 'line1-dotted', linestyle='dotted')
plt.plot(x2,y2, color='red', linewidth = 5,  label = 'line2-dashed', linestyle='dashed')
# show a legend on the plot
plt.legend()
plt.show()
"""