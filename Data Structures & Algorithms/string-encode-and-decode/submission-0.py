class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s): 
            j = i
            # move j until '#'
            while s[j] != "#":
                j += 1
            length = int(s[i:j])      # number before '#'
            j += 1                    # move past '#'
            word = s[j:j+length]      # take length chars
            res.append(word)
            i = j + length            # jump to next encoded word

        return res