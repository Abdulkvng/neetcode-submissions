class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashs = {} #val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashs:
                return[hashs[diff], i ]
            hashs[n] = i
        return
            

            




      # a = nums[0]
        # lens = len(nums)
        # z = lens - 1


        # while a != z:
         

        
        