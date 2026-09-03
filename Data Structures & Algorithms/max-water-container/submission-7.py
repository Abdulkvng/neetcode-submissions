class Solution:
    def maxArea(self, nums: List[int]) -> int:


        lo = 0
        hi = len(nums) -1
        maxarea = 0

        while lo < hi:
            area = min(nums[lo], nums[hi]) * (hi - lo) # height times width
            maxarea = max(area, maxarea)
            if nums[lo] <= nums[hi]:
                lo += 1
            elif nums[lo] > nums[hi]:
                hi -= 1
        
        return maxarea




        