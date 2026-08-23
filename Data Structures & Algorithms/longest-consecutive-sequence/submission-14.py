class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1: return len(nums)
        nums.sort()
        print(nums)
        longest_len = 1
        curr_len = 1
        for i in range(len(nums)):
            # print("+++++++++++++++++++++++++++++")
            # print("Index: " + str(i))
            # print("Longest Len: " + str(longest_len))
            # print("Curr Len: " + str(curr_len))
            # print("+++++++++++++++++++++++++++++")
            if i == 0: continue
            curr_num = nums[i]
            prev_num = nums[i-1]
            if abs(prev_num) == curr_num and prev_num != curr_num:
                diff = 2
            if prev_num != 0 and prev_num < 0 and curr_num > 0:
                diff = 2
            else: 
                diff = abs(abs(curr_num) - abs(prev_num))
            if diff > 1:
                # print("more")
                if longest_len < curr_len:
                    longest_len = curr_len
                curr_len = 1
            elif diff == 0:
                # print("equal")
                if i == len(nums)-1:
                    if longest_len < curr_len:
                        longest_len = curr_len
                continue
            else:
                # print("consec")
                curr_len += 1
                if i == len(nums)-1:
                    if longest_len < curr_len:
                        longest_len = curr_len
        return longest_len