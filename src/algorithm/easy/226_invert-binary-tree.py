# 翻转二叉树
from src.algorithm.data_structures import TreeNode
from typing import Optional
"""
解法：
1. 递归
总结：
元组解包，交换两个变量值
  a,b = b,a
  右侧创建元组(b,a)，解包赋值给左侧
js里也有类似操作，数组解构
  [a,b] = [b,a]
"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        else:
            root.left, root.right = self.invertTree(
                root.right), self.invertTree(root.left)
        return root
