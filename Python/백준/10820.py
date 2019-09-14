import sys

for line in sys.stdin:
    lower = 0
    upper = 0
    number = 0
    space = 0
    li = line

    for x in li:
        if x>='a' and x<='z':
            lower += 1
        elif x>='A' and x<='Z':
            upper += 1
        elif x>='0' and x<='9':
            number += 1
        elif x == ' ':
            space += 1
    print(lower,upper,number,space)

