from SinglyLinkedList import SinglyLinkedList, ListNode

class solution:

    def printList(self, l1):
        print("Printing Linked List:")
        h = l1.head
        while h:
            print(f"val: {h.val}")
            h = h.next

    def find_solution_iterative(self, h1, h2):
        dummy = ListNode(0)
        carry = 0
        curr = dummy

        while h1 or h2 or carry:
            val_1 = h1.val if h1 else 0
            val_2 = h2.val if h2 else 0

            cur_sum = val_1 + val_2 + carry

            if cur_sum >= 10:
                cur_sum = cur_sum % 10
                carry = 1
            else:
                carry = 0

            new_node = ListNode(cur_sum)
            curr.next = new_node
            curr = curr.next

            h1 = h1.next if h1 else h1
            h2 = h2.next if h2 else h2

        return dummy.next

    def find_solution_recursive(self, h1, h2, carry=0):
        if not h1 and not h2 and carry == 0:
            return None
        val_1 = h1.val if h1 else 0
        val_2 = h2.val if h2 else 0
        cur_sum = val_1 + val_2 + carry

        if cur_sum >= 10:
            cur_sum = cur_sum % 10
            carry = 1
        else:
            carry = 0

        new_node = ListNode(cur_sum)
        new_node.next = self.find_solution_recursive(h1.next, h2.next, carry)

        return new_node




if __name__ == "__main__":
    s = solution()

    in_arr_1 = [2,4,3]
    in_arr_2 = [5,6,4]

    l1 = SinglyLinkedList()
    l2 = SinglyLinkedList()
    for n in in_arr_1:
        l1.addAtTail(n)
    for n in in_arr_2:
        l2.addAtTail(n)

    result = s.find_solution_recursive(l1.head, l2.head)

    while result:
        print(result.val)
        result = result.next




