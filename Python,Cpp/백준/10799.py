import sys
A = sys.stdin.readline()
A = A.replace('()','a')

count = 0
sum = 0

for i in range(len(A)):
  if A[i] == '(': 
    count += 1
  elif A[i] == ')': 
    sum += 1  
    count -=1
  elif A[i] == 'a':
     sum += count
  
print(sum)