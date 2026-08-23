class MinStack:

    # def __init__(self):
    #     self.stack = []
    #     self.hashmap = {}

    # def is_empty(self):
    #    return len(self.stack) == 0

    # def push(self, val: int) -> None:
    #     if isinstance(val, int) == True:
    #         self.stack.append(val)
    #         self.hashmap[val] = 1 + self.hashmap.get(val, 0)
    #     else:
    #         self.stack.append(None)
    
    # def top(self) -> int:
    #     if not self.is_empty():
    #         return self.stack[-1]

    # def pop(self) -> None:
    #     if not self.is_empty():
    #         self.hashmap[self.top()] -= 1
    #         self.stack.pop()

    # def getMin(self) -> int:
    #     for num in sorted(self.hashmap):
    #         if self.hashmap[num] > 0:
    #             return num

    def __init__(self):
        self.stack = []
        self.minstack = []

    def is_empty(self):
       return len(self.stack) == 0

    def push(self, val: int) -> None:
        if self.is_empty():
            self.minstack.append(val)
        if isinstance(val, int) == True:
            self.stack.append(val)
            if val < self.minstack[-1]:
                self.minstack.append(val)
            else:
                self.minstack.append(self.minstack[-1])
        else:
            self.stack.append(None)
    
    def top(self) -> int:
        if not self.is_empty():
            return self.stack[-1]

    def pop(self) -> None:
        if not self.is_empty():
            self.minstack.pop() 
            self.stack.pop()

    def getMin(self) -> int:
        return self.minstack[-1]




        
