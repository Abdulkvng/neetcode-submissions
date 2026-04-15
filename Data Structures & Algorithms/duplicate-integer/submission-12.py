class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set1 = []

        for i in nums: 
            if i in set1:
                return True
            else:
                set1.append(i)
        return False


         