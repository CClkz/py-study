# 二叉树的中序遍历

# 题解：
# 1.  递归遍历，递归调用自身，递归结束条件为空节点
# 总结：
# 二叉树遍历：1.前序遍历 2.中序遍历 3.后序遍历 4.层序遍历
# 什么序指根节点在左右子节点的位置
# 1. 前序遍历：根 左 右
# 2. 中序遍历：左 根 右
# 3. 后序遍历：左 右 根
# 4. 层序遍历：第一层、第二层...第N层
# 最开始毫无头绪，其实思考下，只要拼接三个数组， 左 + 节点值 + 右，
# 左右侧可能还有多层节点，结社左侧节点还有多层吧，左侧再调用函数，拼接左侧节点下的 左 + 值 + 右，一层层递归
# 当接收的节点为None时，返回[]
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []

    # 前序遍历
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []

    # 后序遍历
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else []

    # 层序遍历
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res
