'''word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)                    #{'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}

word = 'brontosaurus'
d = dict()
for c in word:
    d[c] = d.get(c,0) + 1
print(d)                     #{'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}'''

'''fhand=open('romeo.txt')
count=dict()
for lines in fhand:
    words=lines.split()
    for word in words:
        if word not in count:
            count[word]=1
        else:
            count[word]=count[word] + 1
print(count)'''

'''fhand=open('mbox-short.txt')
count=dict()
for lines in fhand:
    if lines.startswith('From'):
        line=lines.rstrip()
        words=line.split()
        for words[1] in words:
            count[words[1]]=count.get(words[1],0)+1
print(count)'''

'''stuff = dict()
print(stuff['candy'])
stuff = dict()
print(stuff.get('candy',-1))'''

'''handle = open('mbox-short.txt')
counts = dict()
for line in handle:
    line=line.rstrip()
    if line.startswith('From'):
        words = line.split()[1]
        counts[words] = counts.get(words, 0) + 1
bigcount = 0
bigword = None
smallcount=0
smallword=None
for word, count in list(counts.items()):
    if bigcount == 0 or count > bigcount:
        bigword = word
        bigcount = count
    if smallcount == 0 or count < smallcount:
        smallword = word
        smallcount = count
print(bigword, bigcount,'\n',smallword,smallcount)'''

'''filename = input("Enter a file name: ")
fhand = open(filename, 'r')
counts = dict()

for line in fhand:
    if line.startswith("From "):
        words = line.split()[1]
        counts[words] = counts.get(words, 0) + 1

lrgstemail = None
lrgstfreq = 0
for k in counts:
    if counts[k] > lrgstfreq:
        lrgstemail = k
        lrgstfreq = counts[k]

print(lrgstemail,lrgstfreq )'''

# NEEDS MORE TIME ON THIS PART #