'''fname=input('Enter File Name:- ')
try:
    fhand=open(fname)
except:
    print('Please enter a existing file name with extension. Thank You')
    exit()
#print(fhand)
count=0
for lines in fhand:
    count=count+1
print('line count:', count)
inp=fhand.read()
print(len(inp))
print(inp[:20])
for lines in fhand:
    if lines.startswith('Subject:'):
        count = count + 1
print('There were',count,'subject lines in "',fname,'" file.')

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1: 
        continue
    print(line)
fout=open('output.txt', 'w')
#print(fout)
line1='This is where things getting interesting\n'
print(fout.write(line1))
line2='I have started to write files from Python\n'
print(fout.write(line2))
fout.close()
print(open('output.txt'))
fout=open('output.txt')
for line in fout:
    line=line.rstrip()
    print(line)
fhand = open('words.txt')
for line in fhand:
    line=line.rstrip()
    line = line.upper()
    print(line)

count=0
total=0
fname=input('Enter File Name:- ')
try:
    fhand=open(fname)
except:
    print('Please enter a existing file name with extension. Thank You')
    exit()
for lines in fhand:
    if lines.startswith('X-DSPAM-Confidence:'):
        atpos = lines.find(' ')
        host = lines[atpos+1:]
        flt=float(host)
        total=total+flt
        count=count+1
avg=total/count
print('Average spam confidence: ',avg)
fname=input('Enter File Name:- ')
try:
    fhand=open(fname)
except:
    if fname=='na na boo boo.txt':
        print('NA NA BOO BOO TO YOU- You have been punk"d!')
        quit()
    else:
        print('Please enter a existing file name with extension. Thank You')
        exit()
count=0
for line in fhand:
    if line.startswith('Subject'):
        count=count+1
print('There were',count,'subject lines in"',fname,'" file.')'''