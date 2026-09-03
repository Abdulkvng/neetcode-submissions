class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        cache = []
        n = len(nums)

        for i in range(n):
            lo = i + 1
            hi = n - 1

            while lo < hi:

                if nums[lo] + nums[hi] + nums[i] > 0:
                    hi -= 1
                elif nums[lo] + nums[hi] + nums[i] < 0 :
                    lo += 1
                else:
                    cache.append([nums[i],nums[lo],nums[hi]])
                    lo += 1
                    hi -= 1

        return list(set(tuple(x) for x in cache))
                
                

        