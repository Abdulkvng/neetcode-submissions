class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        cache = Counter(nums)

        heap = []

        for num in cache.keys():
            heapq.heappush(heap, (cache[num],num))

            if len(heap) > k:
                heapq.heappop(heap)
        return [x[1] for x in heap ]








        