class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next

class SinglyLinkedList:

    def __init__(self, print_outcome=False):
        self.size = 0
        self.head = ListNode(0)
        self.print_outcome = print_outcome

    def get(self, index: int, get_value=True):
        if index >= self.size or index < 0:
            print("Invalid index. Operation Cancelled")
            return -1

        node = self.head
        for i in range(index+1):
            node = node.next

        if get_value:
            print(node.val)
            return node.val
        else:
            return node

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            print("Invalid Index. Operation Cancelled")
            return
        if index < 0:
            index = 0
            print("Negative index is not valid; changed to index at 0")

        pred = self.head
        for i in range(index):
            pred = pred.next

        new_node = ListNode(val)
        new_node.next = pred.next
        pred.next = new_node

        self.size += 1
        if self.print_outcome:
            print(f"Added node at index {index}")

    def deleteAtIndex(self, index: int) -> None:
        # Use >= here because if index = size then this is already pointing at None
        if index >= self.size or index < 0:
            print("Invalid index. Operation Cancelled")
            return

        pred = self.head
        for i in range(index):
            pred = pred.next

        pred.next = pred.next.next

        self.size -= 1
        if self.print_outcome:
            print(f"Deleted node at index {index}")

    # Use to create linked list cycles
    def assignNextAtIndex(self, index, next_node):
        if index > self.size:
            print("Invalid Index. Operation Cancelled")
            return
        if index < 0:
            index = 0
            print("Negative index is not valid; changed to index at 0")

        pred = self.head
        for i in range(index+1):
            pred = pred.next

        pred.next = next_node

        self.size += 1
        if self.print_outcome:
            print(f"Assign given node as next node at index {index}")




