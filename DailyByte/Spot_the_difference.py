"""
You are given two strings, s and t which only consist of lowercase letters. t is generated by shuffling the letters in s as well as potentially adding an additional random character. Return the letter that was randomly added to t if it exists, otherwise, return ’ ‘. 
Note: You may assume that at most one additional character can be added to t. 

"""
def spotTheDiff(s,t):
    s1=s2=0
    for i in s:
        s1+=ord(i)
    for i in t:
        s2+=ord(i)
    return chr(abs(s1-s2))

def main():
    for _ in range(int(input())):
        s,t = map(str, input().split())
        print(spotTheDiff(s,t))

if __name__=="__main__":
    main()
