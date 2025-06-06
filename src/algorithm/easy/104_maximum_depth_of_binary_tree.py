# 二叉树的最大深度
from typing import Optional
# 题解：
# 1.  递归遍历
# 根节点为空吗？空返回0，不是空1 + 深度大的子节点深度。
# 子节点深度怎么求？递归调用该方法。
# 总结：
# 最初想了30分钟没思路，突然灵光一闪，想出了递归的思路，还是要多加练习，基础的算法知识要理解透

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
