# 832. Flipping an Image
# https://leetcode.com/problems/flipping-an-image/

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        x, y = len(A), len(A[0])
        for i in range(x):
            A[i] = A[i][::-1]
            for j in range(y):
                A[i][j] ^= 1
        return A


