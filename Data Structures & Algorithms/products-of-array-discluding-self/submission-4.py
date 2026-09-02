class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #initilaize res
        res = [0] * len(nums)

        #create pre 1234 - 1 1 2 6
        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre = pre * nums[i]

        post = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= post
            post *= nums[i]
        
        return res


        



        #create post and multiply by pre

       


        