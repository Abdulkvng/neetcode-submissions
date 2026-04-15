
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result1 = defaultdict(list) #each char count to list of anagrams

        # Go through initial array of strings
        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            result1[tuple(count)].append(s)

        return result1.values()
        