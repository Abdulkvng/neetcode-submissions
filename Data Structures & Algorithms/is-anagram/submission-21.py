class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # go through add to dict -f idct identical true 


        return Counter(s) == Counter(t)
        