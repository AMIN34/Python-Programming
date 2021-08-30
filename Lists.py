'''fruit=['apple','banana','lemon']
print(fruit)
print('adam' in fruit)
print(fruit[0])
numbers = [17, 123]
for i in range(len(numbers)):
    numbers[i]=numbers[i]*2     #updation
print(numbers)
empty=[]
for x in empty:
    print('This never happens')
print(fruit+numbers)        #concatenates= '+' and multiplied or repeatation= '*'

t=['a','b','c','d','e']
print(t[3:])              #['d', 'e']
print(t[1:3])             #['b', 'c']
print(t[:3])              #['a', 'b', 'c']
print(t[:])               #['a', 'b', 'c', 'd', 'e']
#So literally similar to string slices. And yes this is called list slices

t[1:3]=['12','243']        #updated
print(t)                   #['a', '12', '243', 'd', 'e']
t.append('d')
print(t)
fruit=['apple','banana','lemon']
t.extend(fruit)
#print(t)                       #['a', '12', '243', 'd', 'e', 'apple', 'banana', 'lemon']
t.sort()
#print(t)                       #['12', '243', 'a', 'apple', 'banana', 'd', 'e', 'lemon']

x=t.pop(1)
#print(t)                        #['12', 'a', 'apple', 'banana', 'd', 'e', 'lemon'] notice the difference from the previous list
#pop modifies the list and returns the element that was removed. If you don’t provide an index, it deletes and returns the last element.
#print(x)                        #243 the RETURNED Value

del t[1]                         #nothing returned
#print(t)                        #['12', 'apple', 'banana', 'd', 'e', 'lemon'] notice again from the last list

t.remove('banana')               #If you know the element you want to remove (but not the index), you can use remove
#print(t)                         #['12', 'apple', 'd', 'e', 'lemon']

del t[1:3]                       # Slicing delete
print(t)                         #['12', 'e', 'lemon']

numlist=list()
while True:
    line=input('Enter a number:- ')
    if line=='done':
        break
    flt=float(line)
    numlist.append(flt)
average=sum(numlist)/len(numlist)
print('Average:- ',average)

#transformin string into list
s='spam'
print(s)
t=list(s)
print(t)

s= 'I am Lord Voldemort'
t=s.split()               # For breaking into individual words
print(t)                  #['I', 'am', 'Lord', 'Voldemort']

s='pan-pan-pan'
delimeter='-'
t=s.split(delimeter)        #a delimiter that specifies which characters to use as word boundaries
print(t)                    #['pan', 'pan', 'pan']

t=['pan', 'pan', 'pan']
delimeter=' '
print(delimeter.join(t))    #pan pan pan

#printing the "day" only from the file by knowing the structure of the string
fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From '):
        continue
    value=line.split()
    print(value[2])

 #To check whether two variables refer to the same object, you can use the is operator
a= 'banana'
b= 'banana'
print(a is b)    #True

a=['1','2','3']
b=['1','2','3']
print(a is b)    #False

a=['1','2','3']
b=a
print(a is b)     #True
b[0]=45
print(a)          #[45, '2', '3'] Effects both about the changing the element because they are mutable objects unlike strings

def delete_head(t):
    del t[0]
letters=['a','b','c']
delete_head(letters)
print(letters)            #['b', 'c']

def tail(t):
    return t[1:]
letters=['a','b','c']
print(tail(letters))      # ['b', 'c']

def chop(t):
    x=t.pop(0)
    y=t.pop(len(t)-1)
    print(t)
    return None
flist=list()
while True:
    line= input('Enter list element:- ')
    if line=='done':
        break
    flist.append(line)
print(chop(flist))

def middle(t):
    return t[1:len(t)-1]
flist=list()
while True:
    line= input('Enter list element:- ')
    if line=='done':
        break
    flist.append(line)
print(middle(flist))'''

'''word=list()
fhand=open('romeo.txt')
for line in fhand:
    lines=line.split()
    for i in lines:
        if i in word:
            continue
        word=word+[i]
word.sort()
print(word)'''

'''word=list()
count=0
fhand=open('mbox-short.txt')
for lines in fhand:
    if lines.startswith('From') and not lines.startswith('From:'):
        word=lines.split()
        print(word[1])
        count=count+1
print(count)'''

'''number=list()
while True:
    line= input('Enter list element:- ')
    if line=='done':
        break
    number.append(line)
print(float(max(number)))
print(float(min(number)))'''

'''print(list(range(5)))

fruit = 'Banana'
fruit[0] = 'b'
print(fruit)'''
nums=[0,1,2,2,3,0,4,2]
val=2
start,end=0,len(nums)-1
while(start<=end):
    if nums[start]==val:
        nums[start],nums[end],end=nums[end],nums[start],end-1
    else:
        start+=1
print(nums[:start])