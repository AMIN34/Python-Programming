'''import re
fhand= open('mbox-short.txt')
for lines in fhand:
    lines=lines.rstrip()
    x=re.findall('\S+@\S+', lines)
    if len(x)>0:
        print(x)'''


'''import re
fhand= open('mbox-short.txt')
for lines in fhand:
    lines=lines.rstrip()
    x=re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', lines)
    if len(x)>0:
        print(x)'''

'''import re
fhand= open('mbox-short.txt')
for lines in fhand:
    lines=lines.rstrip()
    if re.search('^X\S*: [0-9.]+', lines):             # Note that there is a dot after 9 
        print(lines)'''

'''import re
fhand= open('mbox-short.txt')
for lines in fhand:
    lines=lines.rstrip()
    x=re.findall('^X\S*: ([0-9.]+)', lines)             # Using of parenthesis
    if len(x)>0:
        print(x)'''

'''import re
fhand= open('mbox-short.txt')
for lines in fhand:
    lines=lines.rstrip()
    x=re.findall('^Details: .*rev=([0-9.]+)', lines)         
    if len(x)>0:
        print(x)'''

# ˆ Matches the beginning of the line.

# $ Matches the end of the line.

# . Matches any character (a wildcard).

# \s Matches a whitespace character.

# \S Matches a non-whitespace character (opposite of \s).

# * Applies to the immediately preceding character(s) and indicates to match zero or more times.

# *? Applies to the immediately preceding character(s) and indicates to match zero or more times in “non-greedy mode”.

# + Applies to the immediately preceding character(s) and indicates to match one or more times.

# +? Applies to the immediately preceding character(s) and indicates to match one or more times in “non-greedy mode”.

# ? Applies to the immediately preceding character(s) and indicates to match zero or one time.

# ?? Applies to the immediately preceding character(s) and indicates to match zero or one time in “non-greedy mode”.

# [aeiou] Matches a single character as long as that character is in the specified set. In this example, it would match 
# “a”, “e”, “i”, “o”, or “u”, but no other characters.

# [a-z0-9] You can specify ranges of characters using the minus sign. This example is a single character that must be 
# a lowercase letter or a digit.

# [ˆA-Za-z] When the first character in the set notation is a caret, it inverts the logic. This example matches a single character 
# that is anything other than an uppercase or lowercase letter.

# ( ) When parentheses are added to a regular expression, they are ignored for the purpose of matching, but allow you 
# to extract a particular subset of the matched string rather than the whole string when using findall().

# \b Matches the empty string, but only at the start or end of a word.

# \B Matches the empty string, but not at the start or end of a word.

# \d Matches any decimal digit; equivalent to the set [0-9].

# \D Matches any non-digit character; equivalent to the set [ˆ0-9].

'''import re
fhand= open('mbox.txt')
for lines in fhand:
    lines=lines.rstrip()
    x=re.findall('^New Revision: .*rev=[0-9]+', lines)         
    if len(x)>0:
        print(x)'''

import re
count=0
fhand= open('assignment.txt', 'r')
for lines in fhand:
    lines=lines.rstrip()
    x=re.findall('[0-9]+', lines)
    for i in x:
        count= count+ int(i)                 # Finding Sum of the parsed numbers
print(count)