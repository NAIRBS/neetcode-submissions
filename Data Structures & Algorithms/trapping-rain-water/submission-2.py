class Solution:
    # Have 2 scenarios (from left):
    # 1) l > r, keep extending the bucket
    # 2) l <= r, vol = (r-l-1)*l
    def trap(self, height: List[int]) -> int:
        left, total_vol = 0, 0
        while left < len(height) - 1:
            right = left + 1
            max_right = right
            while right < len(height): # Scan forward from left to find the right bucket wall
                if height[left] <= height[right]:
                    max_right = right
                    break
                if height[right] > height[max_right]:
                    max_right = right
                right += 1
            right = max_right
            if right <= left: break
            displaced_vol = 0   
            for i in range(right - left - 1): # Find the volume taken in between
                displaced_vol += height[left + i + 1] # Skip the left most bucket wall
            total_vol += (((right - left - 1) * min(height[left], height[right])) - displaced_vol)
            left = right # Left bucket wall is now the right bucket wall
        return total_vol