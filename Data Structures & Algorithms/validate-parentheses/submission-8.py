class Solution: # 2nd Oct Revision
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(":
                stack.append(char)
            if char == ")":
                if not stack or stack.pop() != "(": 
                    return False
            if char == "{":
                stack.append(char)
            if char == "}":
                if not stack or stack.pop() != "{": 
                    return False
            if char == "[":
                stack.append(char)
            if char == "]":
                if not stack or stack.pop() != "[": 
                    return False
        if stack: return False 
        return True