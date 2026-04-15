
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result1 = defaultdict(list) #each char count to list of anagrams

        my_dict = {}

        # Go through initial array of strings
        # add all to dict after - if library matched group together 
        for s in strs:
            
            count = [0] * 26

            for letter in s:
                count[ord(letter) - ord('a')] += 1

            result1[tuple(count)].append(s)

        return result1.values()
       