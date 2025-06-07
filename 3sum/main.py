from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result: List[List[int]] = []
        n = len(nums)
        
        for i in range(n - 2):
            # If the current value is the same as the one before, skip to avoid duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            x = nums[i]
            left, right = i + 1, n - 1
            
            while left < right:
                s = x + nums[left] + nums[right]
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    # Found a valid triplet
                    result.append([x, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Skip duplicate values for the second number
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicate values for the third number
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        
        return result