import sys

a = sys.stdin.readline()
li = []
li2 = [-1]*26
n = 0

for x in range(len(a)-1):
    li.append(a[x:x+1])

for idx,x in enumerate(li):
    n = ord(x) - ord('a')
    if li2[n] == -1:
        li2[n] = idx

for x in li2:
    print(x,end=" ")