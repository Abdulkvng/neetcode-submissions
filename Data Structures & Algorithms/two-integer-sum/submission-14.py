class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        cache = {}

        for num in range(len(nums)):
            diff = target - nums[num]
            if diff in cache:
                return [cache[diff],num]
            else:
                cache[nums[num]] = num
        