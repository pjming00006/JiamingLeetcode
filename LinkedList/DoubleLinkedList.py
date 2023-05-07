class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

class DoubleLinkedList:

    def __init__(self):
        self.size = 0

        self.head = ListNode(0)
        self.tail = ListNode(0)

        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, index: int, get_value=True):
        node = None
        if index >= self.size or index < 0:
            print("Invalid index. Operation cancelled")
            return -1

        if self.size == 0:
            print("List is empty. Operation cancelled")
            return node

        if index < self.size - index:
            curr = self.head
            for i in range(index+1):
                curr = curr.next

        else:
            curr = self.tail
            for i in range(self.size - index):
                curr = curr.prev

        node = curr

        if get_value:
            if node:
                return node.val
            else:
                return node
        else:
            return node

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        prev = self.head
        curr = self.head.next

        new_node.prev = prev
        new_node.next = curr
        prev.next = new_node
        curr.prev = new_node
        self.size += 1
        print("Added node at head")

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        prev = self.tail.prev
        tail = self.tail

        new_node.prev = prev
        new_node.next = tail
        prev.next = new_node
        tail.prev = new_node
        self.size += 1
        print("Added node at tail")


    def addAtIndex(self, index: int, val: int) -> None:
        # Here we use index > size not >= size because sometimes we can insert at value where it used to be a dummy tail
        if index > self.size:
            print("Invalid Index. Operation Cancelled")
            return
        if index < 0:
            index = 0
            print("Negative index is not valid; changed to index at 0")

        # Can not use self.get here because self.get does not include dummies in its results
        if index < self.size - index:
            curr_node = self.head
            for i in range(index):
                curr_node = curr_node.next
        else:
            curr_node = self.tail
            for i in range(self.size - index + 1):
                curr_node = curr_node.prev

        next_node = curr_node.next
        new_node = ListNode(val)

        new_node.prev = curr_node
        new_node.next = next_node
        curr_node.next = new_node
        next_node.prev = new_node

        self.size += 1
        print(f"Added node at index {index}")

    def deleteAtIndex(self, index: int) -> None:
        # Use >= here because if index = size then this is already pointing at None
        if index >= self.size or index < 0:
            print("Invalid index. Operation Cancelled")
            return

        to_delete = self.get(index, False)

        next_node = to_delete.next
        prev_node = to_delete.prev

        prev_node.next = next_node
        next_node.prev = prev_node

        self.size -= 1
        print(f"Deleted node at index {index}")


l1 = DoubleLinkedList()
l1.addAtHead(4)
l1.addAtHead(1)
l1.addAtHead(5)
l1.deleteAtIndex(3)
l1.addAtHead(7)
l1.addAtHead(1)

h = l1.head
while h:
    print(f"val: {h.val}")
    h = h.next

l1.deleteAtIndex(4)

h = l1.head
while h:
    print(f"val: {h.val}")
    h = h.next



