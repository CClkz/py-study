# 相交链表

from src.algorithm.data_structures import ListNode
from typing import Optional
# 解法：
# 1.hash表，双层遍历的简化，时间复杂度O(m+n)
# 2.双指针路径补偿，时间复杂度O(m+n)
# 链表A 链表B，两个指针分别走A+B和B+A
# 不存在交点时，A+B和B+A始终不等，最终会走到链表末尾，返回None
# 存在交点时，A可看成 a+c ，B可看成 b+c
# 当 a == b 时：
    # 指针1路径：a → c（在c起点相遇）
    # 指针2路径：b → c
    # 此时不需要走拼接部分就会相交
# 当 a != b 时：
    # 指针1完整路径：a → c → b → c（走a + c + b步）
    # 指针2完整路径：b → c → a → c（走b + c + a步）
    # 必然在第二个c的起点相遇
# 总结：
# 第一时间想到双层遍历，O(m*n)，效率太低，多层遍历时要思考下能不能用hash表处理成O(m+n)复杂度
# 双指针这个方法确实想不到，看了题解也是列了数学公式才理解了，更觉得数学理论的必要性


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lists = set()
        while headA:
            lists.add(headA)
            headA = headA.next
        while headB:
            if headB in lists:
                return headB
            else:
                headB = headB.next
        return None

    # 双指针
    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA, pB = headA, headB
        while pA != pB:
            pA = pA.next if pA else headB  # A→B拼接
            pB = pB.next if pB else headA  # B→A拼接
        return pA  # 返回交点或None
