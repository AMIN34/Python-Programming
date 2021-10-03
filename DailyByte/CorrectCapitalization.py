"""
This question is asked by Google. Given a string, return whether or not it uses capitalization correctly. 
A string correctly uses capitalization if all letters are capitalized, no letters are capitalized, or 
only the first letter is capitalized.

Ex: Given the following strings...
"USA", return true
"Calvin", return true
"compUter", return false
"coding", return true

"""

def solve(s):
    if s.isupper():
        return True
    elif s[0].isupper():
        return True
    elif s.islower():
        return True
    return False

if __name__=="__main__":
    for _ in range(int(input())):
        print(solve(input()))