class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:


        left = 0
        set1 = set()

        for right in range(0, len(nums)):

            if nums[right] in set1:
                return True
            
            set1.add(nums[right])

            if right - left >= k:
                set1.remove(nums[left])
                left += 1

        return False