'''
Author: Archie
Date: 2021-08-28 16:45:48
LastEditTime: 2021-08-28 16:55:11
LastEditors: Archie
FilePath: \LeetCode\7.整数反转.py
'''
#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        tmp = int((str(x) if x > 0 else str(-x) + "-")[::-1])
        return tmp if -2 ** 31 < tmp < 2 ** 31 - 1 else 0
# @lc code=end

