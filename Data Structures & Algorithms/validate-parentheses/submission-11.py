'''
([[{}]])

{()[()()]}

LIFO
open_braces_stack = []

#s = "[]"
s = "]]]]]"
for char in s:
    if char == "[":
        open_braces_stack.append("[")
    elif char == "]":
        if open_braces_stack and open_braces_stack.pop() != "[":
            return False
if open_braces_stack: return False
else: return True
'''

class Solution:
    def isValid(self, s: str) -> bool:
        open_braces_stack = []
        for char in s:
            if char == "[":
                open_braces_stack.append("[")
            elif char == "]":
                if not open_braces_stack or (open_braces_stack and open_braces_stack.pop()) != "[":
                    return False
            elif char == "(":
                open_braces_stack.append("(")
            elif char == ")":
                if not open_braces_stack or (open_braces_stack and open_braces_stack.pop()) != "(":
                    return False
            elif char == "{":
                open_braces_stack.append("{")
            elif char == "}":
                if not open_braces_stack or (open_braces_stack and open_braces_stack.pop()) != "{":
                    return False
            print(open_braces_stack)
        if open_braces_stack: 
            return False
        else: 
            return True