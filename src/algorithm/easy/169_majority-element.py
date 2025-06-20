# 多数元素
from typing import List
# 解法：
# 1. 哈希表法
# 2. 摩尔投票法
# 有人的选票超过半数时可用，
# 记录候选人，下一票和候选人相同，则投票数加1，否则减1，减到0时，更换候选人
# 拓展，找得票超过1/k的人，思路就是先设置k-1个候选人
# 3. 分治法


class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        count_hash: dict[int, int] = {}
        mid = len(nums) / 2
        # n // 2 为向下取整

        for num in nums:
            count_hash[num] = count_hash.get(num, 0) + 1
            if count_hash[num] > mid:
                return num

        return -1

    def majorityElement1(self, nums: List[int]) -> int:
        candidate = nums[0] # 候选
        count = 1
        for num in nums[1:]:
            if count == 0:
                candidate = num
                count = 1
            elif candidate == num:
                count = count + 1
            else:
                count = count - 1
        return candidate 
