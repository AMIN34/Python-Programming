def isPalindrome(s,low,high):
    while low<high:
        if s[low]!=s[high]:
            return False
        low +=1
        high -=1
    return True

def palChecker(s):
    low=0
    high=len(s)-1
    while low<high:
        if s[low]==s[high]:
            low+=1
            high-=1
        else:
            if isPalindrome(s,low+1,high):
                return True
            elif isPalindrome(s,low,high-1):
                return True
            return False
    return True

if __name__=="__main__":
    for _ in range(int(input())):
        print(palChecker(input()))
