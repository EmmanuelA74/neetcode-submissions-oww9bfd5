class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = ans = 0
        freqMap = defaultdict(int)

        for r in range(len(s)):
            freqMap[s[r]] += 1

            while (r - l + 1) - max(freqMap.values()) > k:
                freqMap[s[l]] -= 1
                if freqMap[s[l]] == 0:
                    del freqMap[s[l]]
                
                l += 1
            
            ans = max(ans, r - l + 1)
        
        return ans
