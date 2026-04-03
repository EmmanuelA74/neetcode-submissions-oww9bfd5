class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #monotonically decreasing queue to keep track of the max
        ans = []
        queue = collections.deque()

        for i in range(len(nums)):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            
            queue.append(i)

            #max element is outside the window
            if queue[0] + k == i:
                queue.popleft()
            
            #start tracking max once window reaches appropriate len
            if i >= k - 1:
                ans.append(nums[queue[0]])
        
        return ans 
