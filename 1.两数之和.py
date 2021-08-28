'''
Author: Archie
Date: 2021-08-28 15:41:23
LastEditors: Archie
LastEditTime: 2021-08-28 15:44:43
FilePath: \JavaScriptd:\LeetCode\1.两数之和.py
'''
#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for ind,num in enumerate(nums):
            hashmap[num] = ind
        for i,num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i!=j:
                return [i,j]
# @lc code=end

