# 找到所有数组中消失的数字
from typing import List
"""
题解：
1. set移除
创建set，将1~n加入set中，遍历数组，根据value从set中移除，set剩下的值转为数组
"""


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)
        numbers_set = set(range(1, length + 1))
        for i in range(length):
            if nums[i] in numbers_set:
                numbers_set.remove(nums[i])
        return list(numbers_set)
