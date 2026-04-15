class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        new_cache = {}

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) -  ord('a')] += 1
            key = tuple(count)
            
            if key in new_cache:
                new_cache[key].append(word)
            else:
                new_cache[key] = [word]
            
        return list(new_cache.values())





        
                
        