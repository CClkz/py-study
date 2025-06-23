# 回文链表

from src.algorithm.data_structures import ListNode
from typing import Optional
from src.algorithm.easy.reverse_linked_list_206 import Solution as ReverseSolution

"""
题解：
1. 转成列表，list == list[::-1]判断列表的回文
2. 反转链表 + 双指针
反转链表，再双指针判断是否相等
"""

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list = []
        while head:
            list.append(head.val)
            head = head.next
        return list == list[::-1]

    def isPalindrome1(self, head: Optional[ListNode]) -> bool:
        reverseListNode = ReverseSolution().reverseList(head)
        while head and reverseListNode:
            if head.val != reverseListNode.val:
                return False
            head = head.next
            reverseListNode = reverseListNode.next
        return True
