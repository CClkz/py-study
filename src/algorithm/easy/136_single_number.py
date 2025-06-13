# 只出现一次的数字

from typing import List
from functools import reduce
# 解法
# 1. 异或
# 特性： a^a = 0, a^0 = a, a^b^c = a^c^b
# 所以相同元素的异或都会等于0，最后剩下的就是只出现一次的元素


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # lambda：拉姆达表达式，匿名函数
        # return reduce(lambda a, b: a ^ b, nums)
        return reduce(self.xor, nums)

    def xor(self, a, b):
        return a ^ b
