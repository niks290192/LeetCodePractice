# 1331. Rank Transform of an Array
# https://leetcode.com/problems/rank-transform-of-an-array/

class Solution:
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        rank = {}
        for i, v in enumerate(sorted(set(arr))):
            rank[v] = i + 1
        return [rank[v] for v in arr]