# 二叉树直径
from typing import Optional
from src.algorithm.data_structures import TreeNode


"""
解法：
1. 动态规划
总结：
depNode获取节点深度
        1
      /
    2
  /
3 
节点2的深度是2，作为1的左节点，2的深度也就是1左子树的长度，故 width = left + right
"""


class Solution:
    width = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.width = 0
        self.depNode(root)
        return self.width

    def depNode(self, root: Optional[TreeNode]):
        if not root:
            return 0
        left = self.depNode(root.left)
        right = self.depNode(root.right)
        self.width = max(self.width, left + right)
        return 1 + max(left, right)
