import sys 

N, K= map(int,sys.stdin.readline().split())


li = [0]*N
n = N
count = K
cnt = K

print('<', end='')
while n:  # 7
    if li[count-1] == 0 and cnt == K:
        li[count-1] = 1
        n -= 1
        if n == 0:
            if count == 0 :
                print(N,end='>')
            else :
                print(count,end='>')
        else:
            if count == 0 :
                print(N,end=', ')
            else :
                print(count, end=', ')
        cnt = 0
    else:
        count += 1
        count %= N
        if li[count-1] == 0:
            cnt += 1


import sys
N, K = map(int, input().split()) # 7 3
people = list(range(1, N+1))
result = []
i = K-1    # i = 2
while True:
    result.append(people.pop(i))
    if not people:
        break
    i = (i+K-1) % len(people)   # 2 + 3 - 1 = 4   4 % 6 = 6
    print(i)
    print(people)
print('<'+', '.join(map(str, result))+'>')
