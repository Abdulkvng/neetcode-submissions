class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        goaln = len(nums) // 3

        cache = Counter(nums)

        res = []
        for num in cache:
            if cache[num] > goaln:
                res.append(num)

        return res



        