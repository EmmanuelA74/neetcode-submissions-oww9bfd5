class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            need = target - num

            if need in seen:
                if i < seen[need]:
                    return [i, seen[need]]
                else:
                    return [seen[need], i]
            
            seen[num] = i