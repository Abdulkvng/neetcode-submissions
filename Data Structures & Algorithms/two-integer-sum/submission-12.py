class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashs = {}
        for num in range(len(nums)):
            diff = target - nums[num]
            if diff in hashs:
                return [hashs[diff], num]
            hashs[nums[num]] = num