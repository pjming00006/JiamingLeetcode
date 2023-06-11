from LinkedList.CLASS_SinglyLinkedList import SinglyLinkedList

class StackLinkedList:
    def __init__(self):
        self.stack = SinglyLinkedList()
        self.size = 0

    def push(self, val):
        self.stack.addAtHead(val)
        self.size += 1
        print(f"Push value {val} to the stack.")

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Operation cancelled.")
            return None

        val = self.stack.get(0, True)
        self.stack.deleteAtIndex(0)
        self.size -= 1
        print("Pop from the stack.")
        return val

    def peek(self):
        if self.is_empty():
            print("Stack is empty. Operation cancelled.")
            return None
        return self.stack.get(0, True)

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def printStack(self):
        print("Start printing the stack:")
        head = self.stack.head
        while head:
            print(head.val)
            head = head.next


if __name__ == "__main__":
    s = StackLinkedList()
    s.push(1)
    s.push(3)
    s.push(5)
    s.printStack()
    s.pop()
    s.printStack()