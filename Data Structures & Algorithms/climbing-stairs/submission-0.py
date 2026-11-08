class Solution:
    def climbStairs(self, n: int) -> int:
        # to reach step n, can only arrive from step(n-1) by taking 1 step and step(n-2) by taking 2 steps
        # same relation as fibonacci sequence
        curr_step, prev_step = 1, 1
        for i in range(n-1):
            # temp = curr_step
            # curr_step += prev_step
            # prev_step = temp
            curr_step, prev_step = curr_step + prev_step, curr_step
        return curr_step