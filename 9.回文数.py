'''
Author: Archie
Date: 2021-08-29 10:38:53
LastEditors: Archie Cheng
LastEditTime: 2021-08-29 10:54:02
FilePath: \LeetCode\9.回文数.py
'''
#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x!=0 and x%10==0):
            return False
        right_rev = 0
        while x > right_rev:
            right_rev = right_rev*10 + x %10
            x = x//10
        return x==right_rev or x==right_rev//10
# @lc code=end

