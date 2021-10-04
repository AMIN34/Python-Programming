def palinChecker(s):
    s1=""
    for i  in s:
        if i.isalpha():
            s1+=i
    s1=s1.lower()
    if s1==s1[::-1]:
        return True
    return False
if __name__=="__main__":
    for _ in range(int(input())):
        print(palinChecker(input()))