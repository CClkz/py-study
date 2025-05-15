# 爬楼梯
import math

# 题解：
# 1. 动态规划
# 2. 斐波那契数列公式，有点开挂的的意思，但也可以说见多识广
# 总结：
# 看题解也想了好久才明白，S(n)由S(n-1)、S(n-2)推导的思维确实妙
# 斐波那契数列带来的感悟，数学和写代码之间有什么联系呢
# 或许，算法的内核是数学


class Solution:
    def climbStairs(self, n: int) -> int:
        n1 = 0
        n2 = 1
        n3 = 1
        for i in range(n):
            n3 = n1 + n2
            n1 = n2
            n2 = n3
        return n3

    # 斐波那契数列
    def fibonacci_formula(n):
        sqrt5 = math.sqrt(5)
        phi = (1 + sqrt5) / 2  # 黄金比例
        return int((phi**n - (-phi)**(-n)) / sqrt5)
