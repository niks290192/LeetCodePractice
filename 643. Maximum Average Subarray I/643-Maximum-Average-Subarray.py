# 643. Maximum Average Subarray I
# https://leetcode.com/problems/maximum-average-subarray-i/

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        cur_sum = sum(nums[:k])
        ans = cur_sum
        p1, p2 = 0, k
        while p2 < n:
            cur_sum -= nums[p1]
            cur_sum += nums[p2]
            ans = max(ans, cur_sum)
            p1 += 1
            p2 += 1
        return ans / float(k)