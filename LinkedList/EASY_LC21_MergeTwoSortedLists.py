"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

from CLASS_SinglyLinkedList import ListNode

"""
- Create dummy
- Keep going when either l1 or l2 exist
- If l1 is exhausted, append l2; same for the opposite
- Compare l1 and l2, append smaller one and iterate
"""
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dm = ListNode(next=list1)
        cur = dm
        while list1 or list2:
            if not list1:
                cur.next = list2
                list2 = list2.next
            elif not list2:
                cur.next = list1
                list1 = list1.next
            elif list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        return dm.next

    def mergeTwoListsSimplified(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Time: O(n+m)
        # Space: O(1)
        dm = ListNode(next=list1)
        cur = dm
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        cur.next = list1 if list1 is not None else list2

        return dm.next

    def mergeTwoListsRecurssion(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Time: O(n+m)
        # Space: O(n+m)
        if not list1:
            return list2
        elif not list2:
            return list1
        elif list1.val <= list2.val:
            list1.next = self.mergeTwoListsRecurssion(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoListsRecurssion(list1, list2.next)
            return list2
