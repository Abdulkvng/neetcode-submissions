class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #vertical scanning practice
        res = ""
        if not strs:
            return res
        counter = 0

        for i in range(len(strs[0])): 
            for string in strs:
                if i == len(string) or string[i] != strs[0][i]:
                    return strs[0][:counter]
            counter += 1

        return strs[0][:counter]
            

        
        
