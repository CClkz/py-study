# 环形链表
from typing import Optional
# 解法：
# 1. hash，访问过的存到集合里，后续出现重复的节点，则返回True
# 2. 快慢指针
# 快指针2步，慢指针1步，环形上一定互相的
# 假设快指针在慢指针后面n步，每次前进差距会减1，n次后就会是0相交


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        while head:
            if head in visited:
                return True
            else:
                visited.add(head)
                head = head.next
        return False

    def hasCycle1(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False