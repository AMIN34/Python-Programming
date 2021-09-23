""" Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered. """

# My Solution:-
"""
import re
def increment_string(strng):
    if strng=="":
        return '1'
    x=re.search(r'\d+$',strng)
    # print(x.span())
    if x is None:
        strng+='1'        
    else:
        t=x.span()
        x=strng[t[0]:t[1]]
        l=len(x)
        x=str(int(x)+1)
        if len(x)!=l and len(x)<l:
            x= "0"*(abs(len(x)-l))+x
        strng = strng.replace(strng[t[0]:t[1]], x)
    return strng
"""

# Best Practices
def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "":
        return strng+'1'
    return head + str(int(tail)+1).zfill(len(tail))
print(increment_string("foo99"))