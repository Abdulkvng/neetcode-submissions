class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        hashs = {}
        hasht = {}

        if len(hashs) != len(hasht):
            return False

        for i in range(len(s)):
            hashs[s[i]] = 1 + hashs.get(s[i],0)
            hasht[t[i]] = 1 + hasht.get(t[i],0)
        for x in hashs:
            if hashs[x] != hasht.get(x,0):
                return False
            
        
        return True



        