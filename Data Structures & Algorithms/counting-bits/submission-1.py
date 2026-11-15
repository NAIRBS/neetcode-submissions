class Solution:
    # 1000 = 1,2,4,8,16,32,64,128,256,512 << max 10 bits
    # 1000 (base10) = 111111000
    def countBits(self, n: int) -> List[int]:
        output = []
        for number in range(n + 1):
            count = 0
            for bit in range(32):
                if number & (1 << bit):
                    count += 1
            output.append(count)
        return output