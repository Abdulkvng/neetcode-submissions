class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        newStr = ""

        for char in s:
            if char.isalnum():
                newStr += char.lower()
        

        return newStr[::-1] == newStr


        