class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # go through add to dict -f idct identical true 

        def anagram_counter(string1):

            hashmap = {}

            for char in string1:
                if char in hashmap:
                    hashmap[char] += 1
                else:
                    hashmap[char] = 0
            return hashmap





        return anagram_counter(s) == anagram_counter(t)
        