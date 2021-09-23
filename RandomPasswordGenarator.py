# Random Password generator

import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num="1234567890"
symbols="[],./;*\&#@$!_"
all=lower+upper+num+symbols
length=input("Enter Length of random Password: ")
if len(length)==0:
	length=16
else:
    length=int(length)
password=''.join(random.sample(all,length))
print(password)
