class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # 2 pointers but keep l in lowest

        l, r = 0,1
        maxp = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                prof = prices[r] - prices[l]
                maxp = max(prof, maxp)
            else:
                l = r
            r += 1
        return maxp


        
        