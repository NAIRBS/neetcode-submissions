class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # for i in range(len(s)//2):
        #     holder = s[i]
        #     s[i] = s[len(s)-i-1]
        #     s[len(s)-i-1] = holder

        # Alternatively, we can try the a <> b method, if I recall, the int method is:
        # a = a + b
        # b = a - b << (a+b)-b = a
        # a = a - b << (a+b)-a = b

        for i in range(len(s)//2):
            s[i] = chr(ord(s[i]) + ord(s[len(s)-i-1]))
            s[len(s)-i-1] = chr(ord(s[i]) - ord(s[len(s)-i-1]))
            s[i] = chr(ord(s[i]) - ord(s[len(s)-i-1]))
             
