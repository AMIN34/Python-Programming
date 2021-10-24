"""
Given a string s containing only lowercase letters, continuously remove adjacent characters that are the 
same and return the result.

Ex: Given the following strings...

s = "abccba", return ""
s = "foobar", return "fbar"
s = "abccbefggfe", return "a"
"""
def remove(s:str)-> str:
    d={}
    res=[]
    for i in s:
        d[i] = d.get(i,0)+1
    for k,v in d.items():
        if v%2!=0:
            res.append(k)
    return "".join(res)

if __name__=="__main__":
    for _ in range(int(input())):
        s=input()
        print(remove(s))
