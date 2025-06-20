# 反转链表

from src.algorithm.data_structures import ListNode
from typing import Optional
# 解法：
# 1. 迭代

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newList = None
        while head:
            next_node = head.next
            head.next = newList
            newList = head
            head = next_node
        return newList
