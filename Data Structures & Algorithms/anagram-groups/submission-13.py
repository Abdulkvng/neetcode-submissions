class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        cache = defaultdict(list)

        for string in strs:
            alpha_list = [0] * 26 

            for char in string:
                alpha_list[ord(char) - ord('a')] += 1

            key_tuple = tuple(alpha_list)

            cache[key_tuple].append(string)

        return list(cache.values())
            




        
        