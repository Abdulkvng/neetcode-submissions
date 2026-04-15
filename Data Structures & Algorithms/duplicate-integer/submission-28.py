class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #create new list
        #append to it and if there is return true
        #else add it to new list - return false

    
        # newList = []
        # for i in nums:
        #     if i in newList:
        #         return True
        #     else:
        #         newList.append(i)
        # return False

        newList = []

        for num in nums:
            if num in newList:
                return True
            else:
                newList.append(num)
        return False


    


