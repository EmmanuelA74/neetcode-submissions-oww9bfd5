class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        nums_set = set(nums)

        for num in nums:
            if (num - 1) not in nums_set:
                length = 1
                nxt = num + 1
                while nxt in nums_set:
                    length += 1
                    nxt += 1
                    
                ans = max(ans, length)
        
        return ans