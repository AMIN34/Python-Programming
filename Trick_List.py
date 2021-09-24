""" What will be printed in the output for :- print([0,[1,2,3,4,5][2],2][1]) ?"""

#Solution

print([0,[1,2,3,4,5][2],2][1])

"""
This will print 3 because,   [1,2,3,4,5][2] returns the item or element at index 2 ( Note this is the index not position). So the return value is 3.
So it becomes -> [0,3,2][1] which returns 3 because of the same reasons as the previous.
