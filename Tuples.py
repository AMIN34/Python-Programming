'''t=('a','b','c','d','e')
print(type(t))             #<class 'tuple'>
print(dir(t))'''

'''print(t[1:3])              #('b', 'c')

t[0]='A'
print(t)'''                   #TypeError: 'tuple' object does not support item assignment

'''t=('A',) + t[1:]
print(t)'''                      #('A', 'b', 'c', 'd', 'e')

'''d={'a':30, 'b':20, 'c':10,'e':100}
print(d.items())                     #dict_items([('a', 30), ('b', 20), ('c', 10), ('e', 100)])
print(sorted(d.items()))             #[('a', 30), ('b', 20), ('c', 10), ('e', 100)]
tmp=list()
for k,v in d.items():
    tmp.append((v,k))
print(tmp)                           #[(30, 'a'), (20, 'b'), (10, 'c'), (100, 'e')]
print(sorted(tmp))                   #[(10, 'c'), (20, 'b'), (30, 'a'), (100, 'e')]
print(sorted(tmp, reverse=True))'''    #[(100, 'e'), (30, 'a'), (20, 'b'), (10, 'c')]

'''txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))
    print(t)
    #t.sort(reverse=True)
res = list()
for length, word in t:
    res.append(word)
print(res)'''             #['yonder', 'window', 'breaks', 'light', 'what','soft', 'but', 'in']

'''import string
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))  #From dictionary # need more time
    line = line.lower()
    words = line.split()
for word in words:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))
    lst.sort(reverse=True)
for key, val in lst[:10]:
    print(key, val)'''

'''# Program for finding 10 highest occurable words from a file
fhand=open('romeo.txt')
count=dict()
for lines in fhand:
    words=lines.split()
    for word in words:
        count[word]=count.get(word, 0) + 1
lst=list()                      #
for k,v in count.items():       # This whole part could be written as ""print(sorted([(v,k) for (k,v) in count.items()]))"" if required individually
    lst.append((v,k))           #
print(sorted([(v,k) for (k,v) in count.items()]))
lst=sorted(lst, reverse=True)
for v,k in lst[:10]:
    print(k,v)   '''             # Print 'k' only if you want to print only the key

'''x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
y = x.items()
print(y)
days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[2])'''

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hrs=dict()
for lines in handle:
    if lines.startswith('From') and not lines.startswith('From:'):
        words=lines.split()[5]
        hr=words.split(':')[0]
        hrs[hr]=hrs.get(hr, 0)+1
lst=list()
for h,r in hrs.items():
    lst.append((h,r))
lst.sort()
for h,r in lst:
    print(h,r)