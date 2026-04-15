class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # left and right pointers 
        # sliding window to see if number 
        #and equal or greater is after and then mulitply that to get area (amount of water)
        # return max area gotten 

        result = []
        for i in range(len(heights)):
            l,r = i , len(heights) - 1

            while l < r:
                diff = r - l
                x = min(heights[l], heights[r]) * diff
                result.append(x)
                r -= 1
        return max(result)


                    






        