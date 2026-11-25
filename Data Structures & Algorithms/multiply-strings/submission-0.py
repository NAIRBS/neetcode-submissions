class Solution:
    # Note that its not that we can't do casting, but we can't directly cast input
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        res = [0] * (len(num1) + len(num2)) # The max possible digits
        num1, num2 = num1[::-1], num2[::-1] # LSB becomes MSB, swap order
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2]) # Store result first
                res[i1 + i2] += digit # Add to potentially previous value
                res[i1 + i2 + 1] += res[i1 + i2] // 10 # Move tens digit to front
                res[i1 + i2] = res[i1 + i2] % 10 # Reduce current value to ones digit

        res, beg = res[::-1], 0 # Reverse so MSB turns into LSB (reversed just now)
        while beg < len(res) and res[beg] == 0: # Skip leading zeros!
            beg += 1
        res = map(str, res[beg:]) # Convert each int to char!
        return "".join(res) # Smash it all together into a proper string