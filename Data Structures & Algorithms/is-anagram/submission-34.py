class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hashs = {}
        hasht = {}

        for char in s:
            if char in hashs:
                hashs[char] += 1
            else:
                hashs[char] = 1

        for char in t:
            if char in hasht:
                hasht[char] += 1
            else:
                hasht[char] = 1

        return hashs == hasht
        



        
        