# 对称二叉树

# 题解
# 1. 递归
# 分成左右两个子二叉树，先比根节点值，再比左根的左和右根的右、左根的右和右根的左
# 总结：
# 最开始，想用中序遍历实现，中序遍历等于中序遍历的反转则说明轴对称,但是发现有漏洞，比如：
#      1
#     / \
#    2   2
#   /   /
#  2   2
# 中序遍历为[2,2,1,2,2]，和反转一样但不对称
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, left: TreeNode, right: TreeNode) -> bool:
        if not left and not right:
            return True
        elif not left or not right:
            return False
        else:
            return left.val == right.val and self.isMirror(left.right, right.left) and self.isMirror(left.left, right.right)
