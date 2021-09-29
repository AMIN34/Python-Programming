#Question

"""
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes 
and seconds.

It is much easier to understand with an example:

format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

Detailed rules
The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. 
The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration 
specified by of a component must not be greater than any valid more significant unit of time.
"""

# Method 1)
def format_duration(seconds):
    l,ls=[0]*5,["year","day","hour","minute","second"]
    while seconds!=0:
        if seconds>=(3600*24*365):
            l[0]=seconds//(3600*24*365)
            seconds %= 3600*24*365
        elif seconds>=(3600*24):
            l[1]=seconds//(3600*24)
            seconds %= (3600*24)
        elif seconds >= 3600:
            l[2]=seconds//3600
            seconds %= 3600
        elif seconds >=60:
            l[3]=seconds//60
            seconds %= 60
        else:
            l[4]=seconds
            seconds = 0
    if max(l)==0:
        return "now"
    for i in range(len(l)):
        if l[i]>1:
            ls[i]+="s"
    l=[str(l[i])+" "+ls[i] for i in range(len(l)) if l[i]!=0]
    if len(l)>2:
        return ', '.join(l[:len(l)-1])+" and "+l[len(l)-1]
    else:
        return ' and '.join(l)

# Method 2)
times=[("year",365*24*60*60),("day",24*60*60),("hour",60*60),("minute",60),("second",1)]

def format_duration(seconds):
    if seconds==0:
        return "now"
    l=[]
    for name,secs in times:
        qty = seconds//secs
        if qty:
            if qty>1:
                name += 's'
            l.append(str(qty)+" "+ name)
        seconds %= secs
    return ', '.join(l[:-1]) +" and "+l[-1] if len(l)>1 else l[0]
