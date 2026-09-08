class Solution:
    def maxProfit(self, nums: List[int]) -> int:

        lowest = float('inf')
        maxprof = 0 


        for num in nums:
            if num < lowest:
                lowest = num
            
            profit = num - lowest

            if profit > 0:
                maxprof = max(profit, maxprof)
        
        return maxprof

        
        