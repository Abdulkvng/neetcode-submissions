class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # sort numbers and then return top k
        #hashmap
        # get max value pair and return it
        hashs = {}
        for i in nums:
            if i in hashs:
                hashs[i] += 1
            else:
                hashs[i] =1

        
        # find max value
        maxList = []
        # maxList.append(max(hashs, key= hashs.get))
        for i in range(k):
            currmax = max(hashs, key= hashs.get)
            maxList.append(currmax)
            hashs.pop(currmax)
        # delete from list 

        return maxList






        #     maxList.append(max(hashs, key= lambda x:hash[x]))





