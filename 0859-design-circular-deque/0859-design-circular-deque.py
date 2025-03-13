class MyCircularDeque:

    def __init__(self, k: int):
        self.q = deque()
        self.size = k
        self.cnt =0

    def insertFront(self, value: int) -> bool:
        if len(self.q) == self.size:
            return False
        self.q.appendleft(value)
        self.cnt +=1
        return True


    def insertLast(self, value: int) -> bool:
        if len(self.q) ==self.size:
            return False
        self.q.append(value)
        self.cnt+=1
        return True

    def deleteFront(self) -> bool:
        if len(self.q) == 0:
            return False
        self.q.popleft()
        return True

    def deleteLast(self) -> bool:
        if len(self.q) == 0:
            return False
        self.q.pop()
        return True        

    def getFront(self) -> int:
        if not self.q:
            return -1
        return self.q[0]

    def getRear(self) -> int:
        if not self.q:
            return -1
        return self.q[-1]

    def isEmpty(self) -> bool:
        if len(self.q) == 0:    
            return True
        return False    

    def isFull(self) -> bool:
        if len(self.q) == self.size:
            return True
        return False

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()