class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashs = []

        for i in nums: 
            if i in hashs:
                return True
            else:
                hashs.append(i)
        return False


         