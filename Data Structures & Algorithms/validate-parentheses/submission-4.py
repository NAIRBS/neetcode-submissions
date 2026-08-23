class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False # If it is odd it fails
        # This solution won't work for ()[]{}, it assumes always neatly nested on both ends
        # for i in range(len(s)//2):
        #     opp = len(s)-1-i
        #     if s[i] == "[" and s[opp] == "]": continue
        #     if s[i] == "(" and s[opp] == ")": continue
        #     if s[i] == "{" and s[opp] == "}": continue
        #     return False
        # return True

        # Given ()[]{}, 
        stack = []
        for char in s:
            if char != "]" and char != ")" and char != "}":
                stack.append(char)
            if len(stack) == 0: return False
            if char == "]":
                if stack.pop() != "[": return False
            if char == ")":
                if stack.pop() != "(": return False
            if char == "}":
                if stack.pop() != "{": return False
        if len(stack) != 0: return False
        return True


        