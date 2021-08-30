'''inpstr = input().split(' ')
secretCode = ''
for word in inpstr:
    wordAdded = False
    letterIndex = 0
    while(wordAdded != True):
        if(word.count(word[letterIndex]) > 1):
            letterIndex += 1
        else:
            wordAdded = True
            secretCode = secretCode + word[letterIndex]
print(secretCode.upper())
t={1:'a',2:'b'}
print(t.items())
x=675
print(len(x))'''

List=[4,5,6,7,0,1,2]
target=4
List.sort()
k=len(List)//2
if target<k:
    for i in range(0,k):
        if i==target:
            print(i)
        else:
            print(-1)
else:
    for i in range(k,len(List)+1):
        if i==target:
            print(i)
        else:
            print(-1)