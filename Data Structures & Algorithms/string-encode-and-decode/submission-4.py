class Solution:
      # Let's try a naive solution, we know that we may also be storing numbers
      # Each string is <200 char, we need to compress <100 strings into a single one.
      # Naive solution would be to append all the strings together with spaces...?
      # The string can also contain spaces, so we'd have to replace the space with something else.
      # Basically if strs = "1 2", "3", "4", encrypted will be "1_|2`3`4"


    def encode(self, strs: List[str]) -> str:
        encrypted = ""
        for string in strs:
            if " " in string:
                string.replace(" ", "_|")
            encrypted += string
            encrypted += "`" # This did not work with spaces, I had to use a backtick...
        return encrypted

    def decode(self, s: str) -> List[str]:
        decrypted = []
        start = 0
        stop = 0
        for i in range(len(s)):
            if s[i] == "_" and s[i+1] == "|":
                s[i] = " "
                s = s[:i+1] + s[i+1+1:] # Remove and glue back the "|" element
                i += 1 # Skip the next since it is now gone
                continue

            if s[i] == "`":
                stop = i-1
                decrypted.append(s[start:stop+1])
                start = i+1

        return decrypted
