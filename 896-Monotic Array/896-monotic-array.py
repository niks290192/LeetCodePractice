# Monotonic Array 
# https://leetcode.com/problems/monotonic-array/
# Time O(n), space O(1)

class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        inc, dec = True, True
        for i in range(len(A) - 1):
            if A[i] > A[i+1]:
                inc = False
            if A[i] < A[i+1]:
                dec = False
        return inc or dec

