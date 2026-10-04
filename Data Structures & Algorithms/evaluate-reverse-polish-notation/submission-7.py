class Solution: # 5th Oct Revision
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        for index, value in enumerate(tokens):
            if value == "+":
                result = int(stack.pop()) + int(stack.pop())
                stack.append(result)
            elif value == "-":
                minus = int(stack.pop())
                result = int(stack.pop()) - minus
                stack.append(result)
            elif value == "*":
                result = int(stack.pop()) * int(stack.pop())
                stack.append(result)
            elif value == "/":
                divide = int(stack.pop())
                result = int(int(stack.pop()) / divide)
                stack.append(result)
            else:
                stack.append(value)
        if stack: return int(stack[-1])
        return result
