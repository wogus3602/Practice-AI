num = int(input())

for x in range(num):
  L = list(input())
  while len(L)!=0:
    if L[0] == '(':
      if ')' not in L:
        print("NO")
        break
      L.remove(')')
      L.remove('(')
    else:
      print("NO")
      break
    if len(L) == 0:
      print('YES')
      break
