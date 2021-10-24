"""
Given two strings s and t, which represents a sequence of keystrokes, where # denotes a backspace, return whether or not the sequences produce the same result.

Ex: Given the following strings...

s = "ABC#", t = "CD##AB", return true
s = "como#pur#ter", t = "computer", return true
s = "cof#dim#ng", t = "code", return false
"""
def compare(s:str,t:str)-> bool:
    def bulider(a:str):
        res=[]
        for i in a:
            if i!='#':
                res.append(i)
            else:
                res.pop()
        return "".join(res)
    return bulider(s)==bulider(t)

if __name__=="__main__":
    for _ in range(int(input())):
        s,t = map(str, input().split(" "))
        print(compare(s,t))