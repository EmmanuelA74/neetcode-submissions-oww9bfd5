class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Map, s2Map = defaultdict(int), defaultdict(int)

        for c in s1:
            s1Map[c] += 1
        
        l = 0
        for r in range(len(s2)):
            s2Map[s2[r]] += 1

            while r - l + 1 >= len(s1):
                if s1Map == s2Map:
                    return True
                
                s2Map[s2[l]] -= 1
                if s2Map[s2[l]] == 0:
                    del s2Map[s2[l]]
                
                l += 1
        
        return False