from collections import defaultdict
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

#if not same length then cant be an anagram
        if len(s) != len(t):
            return False
#hash to store both string characters
        hashs = Counter(s)
        hasht= Counter(t)

        if hashs == hasht:
            return True
        return False


        
        