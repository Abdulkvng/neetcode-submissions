class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #counter / dict
        #sort based on values
        #return k elements - nlogk

        cache = Counter(nums)

        sorted_vals = sorted(cache.items(), key = lambda x:x[1], reverse = True)

        return [ x[0] for x in sorted_vals[:k]]
        