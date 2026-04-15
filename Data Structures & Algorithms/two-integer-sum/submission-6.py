class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashs = {} #val : index

        for i in range(len(nums)):
            hashs[nums[i]] = i 
        
        for i in range(len(nums)):
            y = target - nums[i]

            if y in hashs and hashs[y] != i:
                return [i , hashs[y]]


       


        #  for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in hashs:
        #         return[hashs[diff], i]
        #     hashs[n] = i
            

            




      # a = nums[0]
        # lens = len(nums)
        # z = lens - 1


        # while a != z:
         

        
        