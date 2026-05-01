class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        cacheS = {}
        cacheT = {}

        for char in s:
            if char in cacheS:
                cacheS[char] += 1
            else:
                cacheS[char] = 1

        for char in t:
            if char in cacheT:
                cacheT[char] += 1
            else:
                cacheT[char] = 1

        return cacheS == cacheT



        
        