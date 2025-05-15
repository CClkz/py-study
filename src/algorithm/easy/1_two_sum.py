# 两数之和
# 题解：
# 1. 暴力法，两层循环，O(n^2)
# 2. 哈希表，O(n)，hash结构避免了一层循环
# 总结：
# 第一时间想到的就是双层循环，
# 再优化呢，那就是hash，第一层遍历时,已遍历的元素存入hash结构，后面的元素遍历时从hash里找匹配项

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
