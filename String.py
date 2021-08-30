'''word=input('Enter Word:-')
letter=input('Enter a letter ')
def count(letter,word):
    count=0
    for letter in word:
        if letter == 'a':
            count=count+1
    return count
print(count(letter,word))
x='seed'in 'banana'
print(x)
if word== 'banana':
    print('Alright!!!')
elif word < 'banana':
    print('Word comes before banana')
elif word > 'banana':
    print('Word comes after banana')
else:
    print('Alright every banana')'''
#All the uppercase letters come before all the lowercase letters
#print(dir(word))
'''print(word.upper())
print(word.find('na', 3))
print(word.startswith('ba'))
print(word.lower())
print(word.lower().startswith('b')) #CAREFUL WITH THE ORDER
#As long u are careful, we can use multiple callings in a single exprs.'''
'''atpos = word.find(':')
print(atpos)
sppos = word.find('',atpos)
print(sppos)
host = word[atpos+1:sppos]
print(host)
flt=float(host)
print('%g' % flt)
print('%d' % wrd)
#%d to format an integer, %g to format a floating-point number
# %s to format a string
print('In %d years I have increased my effectivity by %g. It is %s' %(3,4,'catching'))
#The number of elements in the tuple must match the number of format sequences in the string'''

nums=[1,3,5,6]
target=7
for i in range(len(nums)-1):
    if nums[i]==target:
        print(i)
        exit()
nums.append(target)
nums.sort()
print(target)
print(nums)
for i in range(len(nums)-1):
    if nums[i]==target:
        print(i)