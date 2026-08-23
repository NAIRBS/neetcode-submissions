class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                newresult = stack.pop() + stack.pop()
                stack.append(newresult)
            elif tokens[i] == "-":
                to_be_subtracted_from = stack.pop()
                newresult = stack.pop() - to_be_subtracted_from
                stack.append(newresult)
            elif tokens[i] == "*":
                newresult = stack.pop() * stack.pop()
                stack.append(newresult)
            elif tokens[i] == "/":
                denominator = stack.pop()
                newresult = int(stack.pop()/denominator)
                stack.append(newresult)
            else:
                stack.append(int(tokens[i]))
        return stack[0]
