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