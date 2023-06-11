from LinkedList.CLASS_SinglyLinkedList import SinglyLinkedList
from LinkedList.CLASS_DoubleLinkedList import DoubleLinkedList


class QueueLinkedList:
    def __init__(self):
        self.queue = DoubleLinkedList()
        self.size = 0

    def enqueue(self, val):
        self.queue.addAtTail(val)
        self.size += 1
        print(f"Added {val} to the queue.")

    def dequeue(self):
        if self.size == 0:
            print("Queue is empty. Operation cancelled.")
            return None

        val = self.queue.get(0, True)
        self.queue.deleteAtIndex(0)
        self.size -= 1
        print(f"Removed {val} from queue.")
        return val

if __name__ == "__main__":
    in_arr = [1,3,5,7,9]
    q = QueueLinkedList()

    for i in in_arr:
        q.enqueue(i)

    for i in range(2):
        print(q.dequeue())
