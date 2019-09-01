import sys
class Deque():
    def __init__(self):
        self.item = []
    def push_front(self,x):
        self.item.insert(0,x)
    def push_back(self,x):
        self.item.append(x)
    def pop_front(self):
        if len(self.item) == 0:
            return -1
        else: return self.item.pop(0)
    def pop_back(self):
        if len(self.item) == 0:
            return -1
        else: return self.item.pop()
    def size(self):
        return len(self.item)
    def empty(self):
        if len(self.item) == 0:
            return 1
        else : return 0
    def front(self):
        if len(self.item) == 0:
            return -1
        else: return self.item[0]
    def back(self):
        if len(self.item) == 0:
            return -1
        else: return self.item[-1]

deque = Deque()

num = int(sys.stdin.readline())

while num:
    A = sys.stdin.readline().split()

    if A[0] == 'push_front':
        deque.push_front(int(A[1]))
    elif A[0] == 'push_back':
        deque.push_back(int(A[1]))
    elif A[0] == 'pop_front':
        print(deque.pop_front())
    elif A[0] == 'pop_back':
        print(deque.pop_back())
    elif A[0] == 'size':
        print(deque.size())
    elif A[0] == 'empty':
        print(deque.empty())
    elif A[0] == 'front':
        print(deque.front())
    elif A[0] == 'back':
        print(deque.back())
    else:
        print("잘못된 값입니다.")

    num -= 1