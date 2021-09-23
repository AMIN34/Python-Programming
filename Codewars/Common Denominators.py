#Question
"""Common denominators

You will have a list of rationals in the form

{ {numer_1, denom_1} , ... {numer_n, denom_n} } 
or
[ [numer_1, denom_1] , ... [numer_n, denom_n] ] 
or
[ (numer_1, denom_1) , ... (numer_n, denom_n) ] 
where all numbers are positive ints. You have to produce a result in the form:

(N_1, D) ... (N_n, D) 
or
[ [N_1, D] ... [N_n, D] ] 
or
[ (N_1', D) , ... (N_n, D) ] 
or
{{N_1, D} ... {N_n, D}} 
or
"(N_1, D) ... (N_n, D)"
depending on the language (See Example tests) in which D is as small as possible and

N_1/D == numer_1/denom_1 ... N_n/D == numer_n,/denom_n.
Example:
convertFracs [(1, 2), (1, 3), (1, 4)] `shouldBe` [(6, 12), (4, 12), (3, 12)]
Note:
Due to the fact that the first translations were written long ago - more than 6 years - these first translations have only irreducible fractions.

Newer translations have some reducible fractions. To be on the safe side it is better to do a bit more work by simplifying fractions even if they don't have to be."""


# My solution
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def find_lcm(a,b):
    return (a*b)//gcd(a,b)

def convert_fracts(lst):
    l=[]
    for i in lst:
        l.append(i[1])
    lcm=1
    for i in l:
        lcm=find_lcm(lcm,i)
    res=[]
    for i in range(len(lst)):
        x=lcm//l[i]
        res.append([lst[i][0]*x,lcm])
    return res

#same but more pythonic
def convertFracts(lst):
    e = 1
    for i in lst:
        e = lcm(e, i[1])
    return [[int(e/i[1])*i[0], e] for i in lst]
    
def gcd(a,b): 
    if a == 0: 
        return b
    return gcd(b % a, a) 
    
def lcm(a,b): 
    return (a*b) / gcd(a,b)
