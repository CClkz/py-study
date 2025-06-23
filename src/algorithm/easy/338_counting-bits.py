# 比特位计数
from typing import List
"""
解法：
1. 逐位计算
转为二进制，统计非零的位数
2. 动态规划
"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        bit_counts = [0]
        for num in range(1, n + 1):
            bit_counts.append(self._count_set_bits(num))
        return bit_counts

    def _count_set_bits(self, num: int) -> int:
        """统计数字二进制表示中1的个数"""
        count = 0
        while num:
            remainder = num % 2
            num = num // 2
            if remainder:
                count += 1
        return count

    def countBits1(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp
