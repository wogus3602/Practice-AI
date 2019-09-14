import sys

num = int(sys.stdin.readline())

li = []
while num:
    A = sys.stdin.readline().split()
    if A[0] == 'push':
        li.append(A[1])
    elif A[0] == 'pop':
        if li: print(li.pop(0))
        else: print('-1')
    elif A[0] == 'size':
        print(len(li))
    elif A[0] == 'empty':
        if len(li) == 0:
            print('1')
        else:
            print('0')
    elif A[0] == 'front':
        if li: print(li[0])
        else: print('-1')
    elif A[0] == 'back':
        if li: print(li[-1])
        else: print('-1')
    else:
        pass
    num -= 1