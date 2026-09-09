class Solution:
    def trap(self, nums: List[int]) -> int:


        maxleft = []
        maxright = len(nums) * [0]
        res = [1] * len(nums)
        water = 0

        pre = 0
        for num in nums:
            maxleft.append(pre)
            pre = max(num,pre)

        post = 0
        for i in range(len(nums)-1,-1,-1):
            maxright[i] = post
            post = max(nums[i],post)
        
        for i in range(len(nums)):
            h = min(maxleft[i], maxright[i])
            water = h - nums[i]
            res[i] = max(water,0)

        return sum(res)

        




        