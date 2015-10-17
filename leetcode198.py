class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        t = nums[0]
        n = 0
        
        for i in range(1, len(nums)):
            (t, n) = (n + nums[i], max(t, n))

        
        return max(t, n)