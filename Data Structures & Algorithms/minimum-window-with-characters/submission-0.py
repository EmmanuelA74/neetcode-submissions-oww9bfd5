class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        sMap, tMap = defaultdict(int), defaultdict(int)

        for c in t:
            tMap[c] += 1
        
        need = len(tMap)
        l = have = 0
        ans = ""

        for r in range(len(s)):
            if s[r] in tMap:
                sMap[s[r]] += 1
                if sMap[s[r]] == tMap[s[r]]:
                    have += 1
            
            while have == need:
                if not ans or (r - l + 1) < len(ans):
                    ans = s[l : r + 1]
                
                if s[l] in tMap:
                    #ignore excess chars
                    if sMap[s[l]] == tMap[s[l]]:
                        have -= 1
                    sMap[s[l]] -= 1
                
                l += 1
        
        return ans
