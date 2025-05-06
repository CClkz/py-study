# 1. 两数之和
# https://leetcode.cn/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]

    def twoSum1(self, nums, target):
        dics = {}
        for i, v in enumerate(nums):
            if (target - v) in dics:
                return [dics[target - v], i]
            else:
                dics[v] = i
