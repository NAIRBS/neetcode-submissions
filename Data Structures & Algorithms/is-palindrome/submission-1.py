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
        newStr = ""
        for char in s:
            if char.isalnum():
                newStr += char.lower() # If alphanumeric, add to string
        return newStr == newStr[::-1] # Compare cleaned string to itself reversed
        