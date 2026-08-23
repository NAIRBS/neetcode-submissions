class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Really crummy o(n^3 solution I guess)
        # output = []
        # for index1, num1 in enumerate(nums):
        #     for index2, num2 in enumerate(nums):
        #         for index3, num3 in enumerate(nums):
        #             if num1 + num2 + num3 == 0 and index1 != index2 and index2 != index3 and index1 != index3:
        #                 add = [num1, num2, num3]
        #                 add.sort()
        #                 if add not in output:
        #                     output.append(add)
        # return output

        # i + j + k = 0
        # i = - (j + k)
        # j + k = -i << we use i as target

        # -1,-2,-3,0,1,2,3
        output = []
        nums.sort()
        print(nums)
        left = 0
        right = len(nums) - 1
        for index, target in enumerate(nums):
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            left = index + 1
            right = len(nums) - 1
            while left < right and index != left and index != right:
                result = -(nums[left] + nums[right])

                if result == target and index != left and index != right:
                    output.append([target, nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                            left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

                elif result < target: right -= 1 
                elif result > target: left += 1

        return output
