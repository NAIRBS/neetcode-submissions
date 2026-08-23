class Solution:
      # Let's try a naive solution, we know that we may also be storing numbers
      # Each string is <200 char, we need to compress <100 strings into a single one.
      # Naive solution would be to append all the strings together with spaces...?
      # The string can also contain spaces, so we'd have to replace the space with something else.
      # Basically if strs = "1 2", "3", "4", encrypted will be "1_|2`3`4" << It passed but cause of my own bugs

      # Second attempt, at the start of each string add a # and a 3 digit number

    def encode(self, strs: List[str]) -> str:
        # encrypted = ""
        # for string in strs:
        #     if " " in string:
        #         string.replace(" ", "_|") # This was done wrongly, so the encryption never happened
        #     encrypted += string
        #     encrypted += "`" # This did not work with spaces, I had to use a backtick...
        # return encrypted
        encrypted = ""
        for strings in strs:
            encrypted += "#"
            no = len(strings)
            formatted_no = f"{no:03d}"[-3:]
            encrypted += formatted_no # Note that len can be up to 3 digits
            encrypted += strings
        encrypted += "_"
        return encrypted


    def decode(self, s: str) -> List[str]:
        # decrypted = []
        # start = 0
        # stop = 0
        # for i in range(len(s)):
        #     if s[i] == "_" and s[i+1] == "|": # No encryption so no decryption
        #         s[i] = " " # You can't change a char string like this
        #         s = s[:i+1] + s[i+1+1:] # Remove and glue back the "|" element
        #         i += 1 # Skip the next since it is now gone
        #         continue

        #     if s[i] == "`":
        #         stop = i-1
        #         decrypted.append(s[start:stop+1])
        #         start = i+1

        # return decrypted
        print(s)
        decrypted = []
        start, stop = 0,0
        i = 0
        while i < len(s) - 1:  # You cannot change i in a for loop, so use a while loop
            if s[i] == "#":
                start = i + 4
                # if i+4 > len(s)-1:
                #     stop = i + 4
                # else: stop = i + 4 + int(s[i+1:i+4])
                stop = i + 4 + int(s[i+1:i+4])
                decrypted.append(s[start:stop])
                i += 4 + int(s[i+1:i+4])
        return decrypted