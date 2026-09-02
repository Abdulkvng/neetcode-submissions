class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        res = set(nums)
        longest = 0 

        for i in res:
            if (i-1) not in res:
                length = 1
                while (i + length) in res:
                    length += 1
                longest = max(length,longest)
        return longest

        