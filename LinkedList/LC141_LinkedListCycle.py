import SinglyLinkedList as linkedlist


class Solution:
    # Brute Force
    def hasCycle(self, head: [linkedlist.ListNode]) -> bool:
        # Brute Force
        if not head or not head.next:
            return False
        hm = {}
        cnt = 0
        while head:
            if head in hm:
                return True
            hm[head] = cnt
            cnt += 1
            head = head.next
        return False

    def hasCylceTwoPointer(self, head):
        # Two Pointers
        if not head or not head.next or not head.next.next:
            return False
        slow, fast = head, head.next.next

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    l1 = linkedlist.SinglyLinkedList()
    for i in [1,3,5,7,9]:
        l1.addAtTail(i)
    l1.assignNextAtIndex(4, l1.get(1, False))

    l2 = linkedlist.SinglyLinkedList()
    for i in [1,3,5,7,9]:
        l2.addAtTail(i)

    res = sol.hasCylceTwoPointer(l1.head)
    res1 = sol.hasCylceTwoPointer(l2.head)
    print(res, res1)