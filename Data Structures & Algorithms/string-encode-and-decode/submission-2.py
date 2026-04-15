class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            #length - seperator and word
            res += "#"
            res += str(len(word))
            if len(str(len(word))) == 1: 
                res += "  "
            if len(str(len(word))) == 2: 
                res += " "

            
            res += str(word)
        return res


    #4neet#4code#4love#3you
    def decode(self, s: str) -> List[str]:
        l = 0
        res = []

        while l < len(s):
            if s[l] == "#":
                substr = s[l+1:l+4]
                k = int(substr.strip())
                start = l+4
                end = l + 4 + k
                res.append(s[start:end])
                l = end
        print(res)
        return res





