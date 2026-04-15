class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}

        cacheS = Counter(s)
        cacheT = Counter(t)

        return cacheS == cacheT