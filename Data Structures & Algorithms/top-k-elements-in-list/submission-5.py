class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #create heap 
        # insert all nums
        count = {}

        for i in nums:
            if i not in count:
                count[i] = 0
            count[i] += 1

        heap = []

        for num in count.keys():

            heapq.heappush(heap, (count[num], num))
            heapq.heapify(heap)

            if len(heap) > k:
                heapq.heappop(heap)


        return [ x[1] for x in heap ]







        #counter / dict
        #sort based on values
        #return k elements - nlogk

        # cache = Counter(nums)

        # sorted_vals = sorted(cache.items(), key = lambda x:x[1], reverse = True)

        # return [ x[0] for x in sorted_vals[:k]]
        