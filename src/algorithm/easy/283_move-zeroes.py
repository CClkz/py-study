# 移动零
from typing import List
"""
题解：
1. 前置法 + 冒泡
总结：
最开始想到的是遍历，切割数组加结尾加元素
相比下，前置法更好
题解里还提供了交换位置，这也很巧妙，不用前置后再遍历一次置零了，0冒泡了
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = 0
        pos = 0  # 记录非零元素应放置的位置
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]  # 交换位置
                pos += 1
