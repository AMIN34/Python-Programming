'''a=input()
lens=len(a)
if(lens>1):
    for i in a:
        if i !='C' or i!='G' or i!='A' or i!='T':
            print('Invalid Input')
            quit()
    for i in a:
        if i =='C':
            print('G', end='')
        elif i =='G':
            print('C', end='')
        elif i =='A':
            print('U', end='')
        elif i =='T':
            print('A', end='')
else:
    if a =='C':
        print('G', end='')
    elif a =='G':
        print('C', end='')
    elif a =='A':
        print('U', end='')
    elif a =='T':
        print('A', end='')
    else:
        print('Invalid Input')'''

def swap_case(s):
    k=list()
    t=s.split()
    for i in t:
        for j in i:
            if ((ord(j)>=65) and (ord(j)<=91)):
                j=ord(j)+32
                k.append(j)
            elif((ord(j)>=97) and (ord(j)<=123)):
                j=ord(j)-32
                k.append(j)
        i=bytes(k).rstrip(b'\0').decode('ascii')

    return i # Don't know about the question

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)