# 1394. Find Lucky Integer in an Array
# https://leetcode.com/problems/find-lucky-integer-in-an-array/

from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = {}
        for num in arr:
            d[num] = d.get(num, 0) + 1
        for k, v in d.items():
            if k == v and k > 0:
                return k
        return -1