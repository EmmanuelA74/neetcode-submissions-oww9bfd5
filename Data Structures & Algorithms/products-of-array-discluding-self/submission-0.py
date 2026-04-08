class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        pre, suff = 1, 1

        for i in range(len(nums)):
            ans[i] = pre
            pre *= nums[i]
        
        for j in range(len(nums) - 1, -1, -1):
            ans[j] *= suff
            suff *= nums[j]
        
        return ans