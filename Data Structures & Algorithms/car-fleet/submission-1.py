class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # (Target - Position)/Car Speed = Number of iterations needed (ROUND UP!!)
        # Cars cannot overtake each other...
        # position =   [4,1,0,7], speed = [2,2,1,1], target = 10
        # Iterations = [3,5,10,3]
        pair = [(p, s) for p, s in zip(position,speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]: 
                stack.pop()
        return len(stack)
