class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class SinglyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = ListNode(0)

    def get(self, index: int) -> int:
        if index > self.size or index < 0:
            print("Invalid index. Operation Cancelled")
            return -1

        node = self.head
        for i in range(index+1):
            node = node.next
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
        print(f"Deleted node at index {index}")
