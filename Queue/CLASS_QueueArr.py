
class QueueArr:
    def __init__(self, print_outcome=False):
        self.queue = []
        self.size = 0
        self.print_outcome = print_outcome

    def enqueue(self, val):
        self.queue.append(val)
        self.size += 1

        if self.print_outcome:
            print(f"Added {val} to the queue.")

    def dequeue(self):
        if self.size == 0:
            print("Queue is empty. Operation cancelled.")
            return None

        val = self.queue[0]
        self.queue = self.queue[1:]
        self.size -= 1
        return val


if __name__ == "__main__":
    q = QueueArr()
    in_arr = [1,3,5,7,9]
    for i in in_arr:
        q.enqueue(i)

    for i in range(2):
        print(q.dequeue())