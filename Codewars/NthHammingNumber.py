"""Haming number is a number made up of 2^i*3^j*5^k, where i, j and k are whole number
i.e. Numbers having prime factors of 2,3,5"""

def hamming(n):
    bases=[2,3,5]
    expos=[0,0,0]
    hams=[1]
    for _ in range(1,n):
        next_hams = [bases[i]*hams[expos[i]] for i in range(3)]
        next_ham =min(next_hams)
        hams.append(next_ham)
        for i in range(3):
            expos[i] += int(next_hams[i]==next_ham)
    return hams[-1]

def main():
    hamming(int(input()))

if __name__=="__main__":
    main()