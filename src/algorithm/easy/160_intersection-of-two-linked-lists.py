# 相交链表

from src.algorithm.data_structures import ListNode
from typing import Optional

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