class Solution:
#     def climbStairs(self, n: int) -> int:
#         one, two = 1, 0

#         for i in range(n):
#             temp = one
#             one = one + two
#             two = temp

#         return one
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)

        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]