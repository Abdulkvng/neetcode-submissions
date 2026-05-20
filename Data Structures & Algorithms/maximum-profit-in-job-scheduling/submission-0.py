class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        index = list(range(n))
        index.sort(key=lambda i: startTime[i])

        cache = [-1] * n

        def dfs(i):
            if i == n:
                return 0
            if cache[i] != -1:
                return cache[i]

            res = dfs(i + 1)

            left, right, j = i + 1, n, n
            while left < right:
                mid = (left + right) // 2
                if startTime[index[mid]] >= endTime[index[i]]:
                    j = mid
                    right = mid
                else:
                    left = mid + 1

            cache[i] = res = max(res, profit[index[i]] + dfs(j))
            return res

        return dfs(0)
