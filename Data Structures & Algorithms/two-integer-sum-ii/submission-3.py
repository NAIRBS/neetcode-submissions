class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Non decreasing order means ascending or the same
        # E.g. 1,2,2,3 or even 1,2,2,2 or 2,2,2,2 or 1,2,3,4
        # Let's use a hashmap I guess
        # numcount = {}
        # for i in range(len(numbers)):
        #     if numbers[i] not in numcount:
        #         numcount[numbers[i]] = []
        #     numcount[numbers[i]].append(i)

        # for key, value in numcount.items():
        #     remainder =  target - key
        #     if remainder in numcount:
        #         if value[0] == numcount[remainder][0] and len(numcount[remainder]) > 1:
        #             return [value[0]+1, numcount[remainder][1]+1]
        #         return [value[0]+1, numcount[remainder][0]+1] # Add 1 for 1-indexed results


        # The real model ans, takes up o(1) space instead of o(n)
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []
  
        