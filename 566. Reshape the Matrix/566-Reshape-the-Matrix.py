# 566. Reshape the Matrix
# https://leetcode.com/problems/reshape-the-matrix/

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        : type r: int
        : type c: int
        :rtype: List[List[int]]
        """
        m, n = len(nums), len(nums[0])
        if m * n != r * c:
            return nums
        ans = [[0 for _ in range(c)] for _ in range(r)]
        p1, p2 = 0, 0
        for i in range(m):
            for j in range(n):
                ans[p1][p2] = nums[i][j]
                p2 += 1
                if p2 == c:
                    p1 += 1
                    p2 = 0
        return ans