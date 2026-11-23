class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = digits[-1]
        digits = digits[::-1]
        output = []
        for i in range(1, len(digits)):
            number += (10 ** i) * digits[i]
        number += 1
        while number > 0:
            digit = number%10
            output.append(digit)
            number //= 10
        return output[::-1]