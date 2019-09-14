import sys

a = sys.stdin.readline()
li = []
li2 = [0]*26
n = 0

for x in range(len(a)-1):
    li.append(a[x:x+1])

for x in li:
    n = ord(x) - ord('a')
    li2[n] += 1

for x in li2:
    print(x,end=" ")