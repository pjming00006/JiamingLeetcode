import CLASS_SinglyLinkedList as linkedlist

class solution:

    def printList(self, l1):
        print("Printing Linked List:")
        h = l1.head
        while h:
            print(f"val: {h.val}")
            h = h.next

    def find_solution_iterative(self, head):
        if not head or not head.next:
            return head

        prev_node = None
        curr_node = head

        while curr_node:
            next_node = curr_node.next

            curr_node.next = prev_node

            prev_node = curr_node
            curr_node = next_node

        return prev_node

    def find_solution_recursive(self, head):
        if not head or not head.next:
            return head

        sub_list = self.find_solution_recursive(head.next)
        head.next.next = head
        head.next = None
        return sub_list


if __name__ == "__main__":
    s = solution()

    in_arr = [1,1,2,3]
    l1 = linkedlist.SinglyLinkedList()
    for n in in_arr:
        l1.addAtTail(n)
    # s.printList(l1)
    result = s.find_solution_recursive(l1.head)

    while result:
        print(result.val)
        result = result.next




