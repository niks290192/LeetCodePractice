# 674. Longest Continuous Increasing Subsequence
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/


class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        dp = [0] * len(nums)
        for i in range(len(nums)):
            dp[i] = 1
            if i > 0 and nums[i] > nums[ i - 1 ]:
                dp[i] = max(dp[i], dp[i - 1] + 1)
        return max(dp)