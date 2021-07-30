# 448. Find all numbers Disappeared in an Array
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/


class Solution(object):
    def findDisappearedNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            new_index = abs(nums[i]) - 1
            if nums[new_index] > 0:
                nums[new_index] *= -1
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)
        return ans