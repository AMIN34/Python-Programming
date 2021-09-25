"""
Description:
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))
"""

# Method 1)
def zero(op=None):
    if op==None:
        return 0
    else:
        return op(0) 
def one(op=None):
    if op==None:
        return 1
    else:
        return op(1)
def two(op=None):
    if op==None:
        return 2
    else:
        return op(2)
def three(op=None):
    if op==None:
        return 3
    else:
        return op(3)
def four(op=None):
    if op==None:
        return 4
    else:
        return op(4)
def five(op=None):
    if op==None:
        return 5
    else:
        return op(5)
def six(op=None):
    if op==None:
        return 6
    else:
        return op(6)
def seven(op=None):
    if op==None:
        return 7
    else:
        return op(7)
def eight(op=None):
    if op==None:
        return 8
    else:
        return op(8)
def nine(op=None):
    if op==None:
        return 9
    else:
        return op(9)
def plus(op):
    return lambda y:y+op
def subtract(op):
    return lambda y:y-op
def multiply(op):
    return lambda y:y*op
def dividedby(op):
    return lambda y:y/op

if __name__=="__main__":
    print(seven(plus(three())))
	
# Method 2)
def identity(a):
	return a
def zero(f=identity): 
	return f(0)
def one(f=identity): 
	return f(1)
def two(f=identity): 
	return f(2)
def three(f=identity): 
	return f(3)
def four(f=identity): 
	return f(4)
def five(f=identity): 
	return f(5)
def six(f=identity): 
	return f(6)
def seven(f=identity): 
	return f(7)
def eight(f=identity): 
	return f(8)
def nine(f=identity): 
	return f(9)

def plus(b): return lambda a: a + b
def minus(b): return lambda a: a - b
def times(b): return lambda a: a * b
def divided_by(b): return lambda a: a // b

# Method 3)
def zero(arg=""):  return eval("0" + arg)
def one(arg=""):   return eval("1" + arg)
def two(arg=""):   return eval("2" + arg)
def three(arg=""): return eval("3" + arg)
def four(arg=""):  return eval("4" + arg)
def five(arg=""):  return eval("5" + arg)
def six(arg=""):   return eval("6" + arg)
def seven(arg=""): return eval("7" + arg)
def eight(arg=""): return eval("8" + arg)
def nine(arg=""):  return eval("9" + arg)

def plus(n):       return "+%s" % n
def minus(n):      return "-%s" % n
def times(n):      return "*%s" % n
def divided_by(n): return "/%s" % n
