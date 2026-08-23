class MinStack:

    def __init__(self):
        self.stack = []
        self.lowest = math.inf
        self.hashmap = {}

    def is_empty(self):
       return len(self.stack) == 0

    def push(self, val: int) -> None:
        if isinstance(val, int) == True:
            self.stack.append(val)
            self.hashmap[val] = 1 + self.hashmap.get(val, 0)
            if val <= self.lowest:
                self.lowest = val
        else:
            self.stack.append(None)
    
    def top(self) -> int:
        if not self.is_empty():
            return self.stack[-1]

    def pop(self) -> None:
        if not self.is_empty():
            self.hashmap[self.top()] -= 1
            self.stack.pop()

    def getMin(self) -> int:
        for num in sorted(self.hashmap):
            if self.hashmap[num] > 0:
                return num


        
