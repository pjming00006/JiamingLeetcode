import CLASS_SinglyLinkedList as linkedlist

class solution:

    def printList(self, l1):
        print("Printing Linked List:")
        h = l1.head
        while h:
            print(f"val: {h.val}")
            h = h.next

    def find_solution(self, l1):
        prev = l1.head.next

        if not prev:
            return l1.head

        if not prev.next:
            return prev

        curr = prev.next

        # Approach 1: remove dupe one by one
        # while curr:
        #     if curr.val == prev.val:
        #         prev.next = curr.next
        #         curr = curr.next
        #     else:
        #         curr = curr.next
        #         prev = prev.next

        # Approach 2: Remove all dupes at once since list is sorted
        while curr:
            if curr.val == prev.val:
                curr = curr.next
            else:
                prev.next = curr
                prev = curr
                curr = curr.next
        prev.next = curr

        return l1.head


if __name__ == "__main__":
    s = solution()

    in_arr = [1,1,2,3,3,4,4,4,5]
    l1 = linkedlist.SinglyLinkedList()
    for n in in_arr:
        l1.addAtTail(n)
    s.printList(l1)
    s.find_solution(l1)
    s.printList(l1)



