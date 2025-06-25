# 汉明距离
# 理查德·汉明提出
from typing import List
"""
题解:
1. 转二进制数组，数值小的补零再比较
2. 异或运算，结果二进制为1的个数
总结：
处理十进制数值的二进制格式，不一定要转二进制数组，可以用>>=1来移位
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        max = x if x > y else y
        min = x if x < y else y
        li1 = self.toBits(max)
        li2 = self.toBits(min)

        padding_length = len(li1) - len(li2)
        li2 += [0] * padding_length

        count = 0
        for i in range(len(li1)):
            v2 = li2[i] if li2[i] else 0
            if li1[i] != v2:
                count += 1

        return count

    def toBits(self, num: int) -> List[int]:
        li = []
        while num:
            remainder = num % 2
            num = num // 2
            if remainder:
                li.append(1)
            else:
                li.append(0)
        return li

    def hammingDistance1(self, x: int, y: int) -> int:
        xor_result = x ^ y  # 异或运算得到差异位
        distance = 0
        while xor_result:
            distance += xor_result & 1  # 统计最低位的1
            xor_result >>= 1  # 右移一位
        return distance
