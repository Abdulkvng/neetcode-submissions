class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # everthing times itself subtract for the item 
        zero_count = nums.count(0)

        product = 1
        res = []

        if zero_count < 1:
            for num in nums:
                product *= num
            return [ product // x for x in nums]

        if zero_count == 1:
            for num in nums:
                if num == 0:
                    continue
                else:
                    product *=num
            
            for num in nums:
                if num == 0:
                    res.append(product)
                else:
                    res.append(0)
            return res


        if zero_count > 1:
            return [0] * len(nums)
                    




      