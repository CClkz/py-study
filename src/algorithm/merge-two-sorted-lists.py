# 21. 合并两个有序链表
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Optional[X] 等价于 Union[X, None]，表示一个值可以是类型 X，也可以是 None

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        