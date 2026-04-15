class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hs = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in hs:
                return [ hs[diff], i]
            hs[num] = i

        