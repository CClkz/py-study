# 合并两个有序链表
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Optional[X] 等价于 Union[X, None]，表示一个值可以是类型 X，也可以是 None


class Solution:
    # 双指针
    # 时间复杂度 O(n + m)
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        newList: Optional[ListNode] = None
        p1 = list1
        p2 = list2

        if p1 and p2:
            if p1.val <= p2.val:
                newList = p1
                p1 = p1.next
            else:
                newList = p2
                p2 = p2.next
        elif p1:
            return p2
        elif p2:
            return p1

        cNode = newList

        while p1 or p2:
            if cNode is not None:
                if p1 and p2:
                    if p1.val <= p2.val:
                        cNode.next = p1
                        p1 = p1.next
                    else:
                        cNode.next = p2
                        p2 = p2.next
                elif p1:
                    cNode.next = p1
                    p1 = p1.next
                elif p2:
                    cNode.next = p2
                    p2 = p2.next

                cNode = cNode.next
            else:
                break

        return newList

    # 双指针，优化
    def mergeTwoLists1(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # 使用虚拟头节点简化操作
        dummy = ListNode()
        current = dummy

        # 注意用and不用or，这样有一个链表查完了，另一个链表剩余部分不需要循环了、直接拼接
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # 将剩余链表直接接上
        current.next = list1 if list1 else list2

        return dummy.next

    # 遍历法
    def mergeTwoLists2(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        node = ListNode()

        if list1.val <= list2.val:
            node.val = list1.val
            node.next = self.mergeTwoLists2(list1.next, list2)
        else:
            node.val = list2.val
            node.next = self.mergeTwoLists2(list1, list2.next)

        return node

    # 遍历法，题解
    def mergeTwoLists3(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists3(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists3(l1, l2.next)
            return l2
