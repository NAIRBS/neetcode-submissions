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

        # This works, but it doesn't really match with the given solution, I guess tricks like this aren't good...
        # Time: O(n/2) = O(n), same as solution
        # Space: log(1), but I don't use temp var so it's better than the model solution
        # for i in range(len(s)//2):
        #     s[i] = chr(ord(s[i]) + ord(s[len(s)-i-1]))
        #     s[len(s)-i-1] = chr(ord(s[i]) - ord(s[len(s)-i-1]))
        #     s[i] = chr(ord(s[i]) - ord(s[len(s)-i-1]))

        # Let's try this again with 2 pointers since we love pointers I guess
        l,r = 0, len(s)-1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l,r = l+1, r-1             
