class Solution:
    # 1000 = 1,2,4,8,16,32,64,128,256,512 << max 10 bits
    # 1000 (base10) = 111111000
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n+1):
            count = 0
            for bit in range(10, -1, -1):
                if i >= 2**bit:
                    count += 1
                    i -= 2**bit
            output.append(count)
        return output