# 买卖股票的最佳时机
from typing import List
# 解法：
# 1. 一次遍历
# 总结：
# 第一时间想到双指针，但是实现的时候迷糊了，左右两个指针怎么移动呢，同时或者额移动哪一个？走不通
# 再想到两层循环，但是这样解就没意思了
# 最后看了以前的提交记录，回忆起一次便利的方法
#  时间复杂度：O(n)，记录第n天之前的最低值，第n天最大利润就是prices[n] - min，再比较每天的最大利润


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        max = 0
        r = len(prices) - 1
        for val in prices:
            if val < min:
                min = val
            else:
                max = val - min if val - min > max else max
        return max
