from LinkedList.CLASS_SinglyLinkedList import SinglyLinkedList
from LinkedList.CLASS_DoubleLinkedList import DoubleLinkedList


class QueueLinkedList:
    def __init__(self, print_outcome=False):
        self.queue = DoubleLinkedList()
        self.size = 0
        self.print_outcome = print_outcome

    def enqueue(self, val):
        self.queue.addAtTail(val)
        self.size += 1

        if self.print_outcome:
            print(f"Added {val} to the queue.")

    def dequeue(self):
        if self.size == 0:
            print("Queue is empty. Operation cancelled.")
            return None

        val = self.queue.get(0, True)
        self.queue.deleteAtIndex(0)
        self.size -= 1

        if self.print_outcome:
            print(f"Removed {val} from queue.")
        return val

    def print_queue(self):
        head = self.queue.head.next
        out_arr = []
        while head and head.next:
            out_arr.append(head.val)
            head = head.next
        print(out_arr)
        return out_arr


if __name__ == "__main__":
    in_arr = [1,3,5,7,9]
    q = QueueLinkedList()

    for i in in_arr:
        q.enqueue(i)

    q.print_queue()
