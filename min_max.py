total=0
count=0
largest= None
smallest= None
while True:
    line = input('Enter number: ')
    if line == 'done':
        break
    try:
        sk=float(line)
    except:
        print('Invalid Input')
        continue
    if largest is None or line > largest:
        largest = line
    if smallest is None or line<smallest:
        smallest=line
    total=total+sk
    count=count+1
    avg=total/count
print('Total, Count, Average, Max and Min are:- ',total,count,avg,largest,smallest)
largest= None
smallest= None
while True:
    line = input('Enter number: ')
    if line == 'done':
        break
    try:
        num=int(line)
    except:
        print('Invalid input')
        continue
    if largest is None or num > largest:
        largest = num
    if smallest is None or num < smallest:
        smallest=num
print('Maximum is',largest)
print('Minimum is',smallest)