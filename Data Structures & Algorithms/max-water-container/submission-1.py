class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # left and right pointers 
        # sliding window to see if number 
        #and equal or greater is after and then mulitply that to get area (amount of water)
        # return max area gotten 

        
        l,r = 0 , len(heights) - 1
        result = 0
        while l < r:
            diff = r - l
            area = min(heights[l], heights[r]) * diff
            result = max(area, result)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -=1

        return result
       
       
       
        # lets goooooo


                    






        