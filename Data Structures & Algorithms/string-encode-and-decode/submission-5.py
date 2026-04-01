class Solution:

    def encode(self, strs: List[str]) -> str:
        # "#" symbol makes encoding stronger
        encodedStr = ""

        for word in strs:
            encodedStr += str(len(word)) + "#" + word
        
        return encodedStr

    def decode(self, s: str) -> List[str]:
        decodedStr = []
        i = 0
        #while loop to loop and get a single word
        while (i < len(s)):
            j = i
            while s[j] != "#":
                j += 1
            length = s[i:j] #splicing
            i = j + 1
            j = i + int(length)
            decodedStr.append(s[i:j])
            i = j
        
        return decodedStr

