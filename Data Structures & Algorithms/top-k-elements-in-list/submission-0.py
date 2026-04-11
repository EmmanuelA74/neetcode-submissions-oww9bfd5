class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        freqMap = defaultdict(int)
        counts = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            freqMap[num] += 1

        for key, val in freqMap.items():
            counts[val].append(key)
        
        for i in range(len(counts) - 1, -1, -1):
            for key in counts[i]:
                if k == 0:
                    break
                ans.append(key)
                k -= 1

        return ans 
        