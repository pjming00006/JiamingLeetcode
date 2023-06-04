class StackArr:
    def __init__(self):
        self.size = 0
        self.arr = []
        self.min_val = None
        self.max_val = None

    # Add to stack
    def push(self, val):
        self.arr.append(val)
        self.size += 1
        print("Pushed to stack.")

    # Remove from stack
    def pop(self):
        if self.size == 0:
            print("Stack is empty. Operation cancelled.")
        else:
            self.arr.pop()
            self.size -= 1
            print("Popped from stack.")

    # Get the top of the stack
    def top(self):
        if self.size == 0:
            print("Stack is empty. Operation cancelled.")
        else:
            print(f"The top of the stack is {self.arr[-1]}")
            return self.arr[-1]

    def get_min(self):
        print(f"Min is {min(n for n in self.arr)}")
        return min(n for n in self.arr)

    def get_max(self):
        print(f"Max is {max(n for n in self.arr)}")
        return max(n for n in self.arr)

    def print_stack(self):
        print("Printing the stack:")
        print(self.arr)


if __name__ == "__main__":
    my_stack = StackArr()

    in_arr = [1,3,5,7,9]
    for n in in_arr:
        my_stack.push(n)

    my_stack.print_stack()

    my_stack.pop()

    my_stack.get_max()
