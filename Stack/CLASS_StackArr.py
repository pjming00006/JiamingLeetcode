class StackArr:
    def __init__(self):
        self.size = 0
        self.stack = []
        self.min_val = None
        self.max_val = None

    # Add to stack
    def push(self, val):
        self.stack.append(val)
        self.size += 1
        print("Pushed to stack.")

    # Remove from stack
    def pop(self):
        if self.size == 0:
            print("Stack is empty. Operation cancelled.")
            return None
        else:
            val = self.stack[-1]
            self.stack.pop()
            self.size -= 1
            print("Popped from stack.")
            return val

    # Get the top of the stack
    def peek(self):
        if self.size == 0:
            print("Stack is empty. Operation cancelled.")
        else:
            print(f"The top of the stack is {self.stack[-1]}")
            return self.stack[-1]

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def get_min(self):
        print(f"Min is {min(n for n in self.stack)}")
        return min(n for n in self.stack)

    def get_max(self):
        print(f"Max is {max(n for n in self.stack)}")
        return max(n for n in self.stack)

    def print_stack(self):
        print("Printing the stack:")
        print(self.stack)


if __name__ == "__main__":
    my_stack = StackArr()

    in_arr = [2,1]
    for n in in_arr:
        my_stack.push(n)

    my_stack.print_stack()

    my_stack.pop()

    my_stack.print_stack()

    my_stack.get_max()
