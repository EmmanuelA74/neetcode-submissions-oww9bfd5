class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for word in strs:
            encodedString += word
            encodedString += "'"

        return encodedString


    def decode(self, s: str) -> List[str]:
        startIndex = 0
        decodedString = []

        for index in range(0, len(s)):
            if s[index] == "'":
                decodedString.append(s[startIndex:index])
                startIndex = index + 1

        return decodedString

        
                



