from Stack.CLASS_StackArr import StackArr

class QueueWithStacks:
    def __init__(self):
        self.in_stack = StackArr()
        self.out_stack = StackArr()

    def push(self, val):
        self.in_stack.push(val)

    def pop(self):
        if self.out_stack.is_empty():
            for i in range(self.in_stack.size - 1, -1, -1):
                self.out_stack.push(self.in_stack.pop())
            return self.out_stack.pop()
        else:
            return self.out_stack.pop()

    def peek(self):
        if self.out_stack.is_empty():
            for i in range(self.in_stack.size - 1, -1, -1):
                self.out_stack.push(self.in_stack.pop())
            return self.out_stack.peek()
        else:
            return self.out_stack.peek()

    def empty(self):
        if self.in_stack.is_empty() and self.out_stack.is_empty():
            return True
        else:
            return False


if __name__ == "__main__":
    q = QueueWithStacks()

    in_arr = [1,2]
    for i in in_arr:
        q.push(i)
    q.in_stack.print_stack()

    q.peek()

    print(q.pop())
    print(q.empty())

