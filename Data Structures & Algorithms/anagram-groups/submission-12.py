class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = {}
        # want key as tuple of char count 
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            if key in res:
                res[key].append(word)
            else:
                res[key] = []
                res[key].append(word)
            
        return list(res.values())

            
           
            
   


        