from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

#if not same length then cant be an anagram
        if len(s) != len(t):
            return False
#hash to store both string characters
        hashs = defaultdict(int)
        hasht = {}

       
# .get checks the hash to see how many of the char is already there if not it returns 0 
        for i in range(len(s)):
            hashs[s[i]] +=1
            hasht[t[i]] = 1 + hasht.get(t[i], 0)

        if hashs == hasht:
            return True
        return False


        
        