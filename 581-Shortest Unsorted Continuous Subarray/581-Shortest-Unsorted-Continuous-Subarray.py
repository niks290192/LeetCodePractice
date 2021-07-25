# 581 Shortest unsorted continuous subarray 
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr_min, arr_max = float("inf"), -float("inf")
        flag = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                flag = True
            if flag:
                arr_min = min(arr_min, nums[i])
        flag = False
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                flag = True
            if flag:
                arr_max = max(arr_max, nums[i])
        for l in range(len(nums)):
            if nums[l] > arr_min:
                break
        for r in range(len(nums) - 1, -1, -1):
            if nums[r] < arr_max:
                break
        if r - l > 0:
            return r - l + 1
        else:
            return 0