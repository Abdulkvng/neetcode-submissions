class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = {}
        for i in strs:
            count = [0] * 26
            for char in i:
                count[ord('a') -  ord(char)] += 1
            key = tuple(count)

            if key not in res:
                res[key] = []
            res[key].append(i)
        return list(res.values())
            
   


        