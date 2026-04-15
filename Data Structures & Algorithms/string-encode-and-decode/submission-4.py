class Solution:

    def encode(self, strs: List[str]) -> str:

        new_string = ''

        for word in strs:
            new_string += str(len(word)) + "#" + word
        return new_string

    5#Hello5#World
    def decode(self, s: str) -> List[str]:

        decoded_string = []
        lpointer = 0
        while lpointer < len(s):
            rpointer = lpointer
            while s[rpointer] != '#':
                rpointer += 1
            length = int(s[lpointer:rpointer])
            lpointer = rpointer + 1 
            rpointer = lpointer + length
            decoded_string.append(s[lpointer:rpointer])
            lpointer = rpointer

        return decoded_string






            

