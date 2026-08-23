class Solution:
    def isPalindrome(self, s: str) -> bool:
        # reversed = ""
        # s = "".join(c for c in s if c.isalnum()) # Only keep alphanumeric, remove special char + spaces
        # for i in range(len(s)):
        #     reversed += s[len(s)-i-1]
        #     #print(s[len(s)-i-1])
        # if reversed.lower() == s.lower(): return True
        # else: return False

        # Better solution
        # newStr = ""
        # for char in s:
        #     if char.isalnum():
        #         newStr += char.lower() # If alphanumeric, add to string
        # return newStr == newStr[::-1] # Compare cleaned string to itself reversed

        # With 2 array pointers (in place comparison)
        if len(s) == 1: return True
        left = 0
        right = len(s)-1
        while left <= right:
            while s[left].isalnum() == False:
                left += 1
                if left >= len(s): return True
            while s[right].isalnum() == False:
                right -= 1
                if right < 0: return True
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
                continue
            else:
                return False
        return True


        