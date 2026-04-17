class Solution:
    def isValid(self, s: str) -> bool:
        bracMap = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        stack = []

        for c in s:
            if c in bracMap:
                if stack and stack[-1] == bracMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return not stack