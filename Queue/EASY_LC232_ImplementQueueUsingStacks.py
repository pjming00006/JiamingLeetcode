# from Stack.CLASS_StackArr import StackArr
#
# class QueueWithStacks:
#     def __init__(self):
#         self.in_stack = StackArr()
#         self.out_stack = StackArr()
#
#     def push(self, val):
#         self.in_stack.push(val)
#
#     def pop(self):
#         if self.out_stack.is_empty():
#             for i in range(self.in_stack.size - 1, -1, -1):
#                 self.out_stack.push(self.in_stack.pop())
#             return self.out_stack.pop()
#         else:
#             return self.out_stack.pop()
#
#     def peek(self):
#         if self.out_stack.is_empty():
#             for i in range(self.in_stack.size - 1, -1, -1):
#                 self.out_stack.push(self.in_stack.pop())
#             return self.out_stack.peek()
#         else:
#             return self.out_stack.peek()
#
#     def empty(self):
#         if self.in_stack.is_empty() and self.out_stack.is_empty():
#             return True
#         else:
#             return False


class MyQueue:
    def __init__(self):
        self.my_stack = []
        self.tool_stack = []
        self.stack_len = 0

    def push(self, x: int) -> None:
        """
        Time: O(n), Space: O(n)
        If my_stack is empty, append to my_stack
        If not, then pop each from my_stack into tool_stack, then append the new element to my_stack, then add
        elements from tool_stack back to my_stack
        """
        if not self.my_stack:
            self.my_stack.append(x)
            self.stack_len += 1
            return

        while self.my_stack:
            self.tool_stack.append(self.my_stack.pop())
        self.my_stack.append(x)
        while self.tool_stack:
            self.my_stack.append(self.tool_stack.pop())
        self.stack_len += 1

    def pop(self) -> int:
        # Time, Space: O(1)
        self.stack_len -= 1
        return self.my_stack.pop()

    def peek(self) -> int:
        # Time, Space: O(1)
        return self.my_stack[self.stack_len - 1]

    def empty(self) -> bool:
        # Time, Space: O(1)
        return self.stack_len == 0

class MyQueueAmortized:

    def __init__(self):
        self.my_stack = []
        self.tool_stack = []
        self.front = None

    def push(self, x: int) -> None:
        # Time: O(1), Space: O(n)
        if not self.my_stack:
            # This is the front of the partial queue stored in my_stack
            self.front = x
        self.my_stack.append(x)

    def pop(self) -> int:
        """
        During the first pop, we pop everything from my_stack to tool_stack to get reversed order, then pop the
        tool_stack(O(n)). In subsequent pops, as long as tool_stack has values, we can keep popping tool_stack,
        which is O(1). Amortized means that on average, we could reduce the time complexity to O(1)
        """
        if not self.tool_stack:
            while self.my_stack:
                self.tool_stack.append(self.my_stack.pop())
        return self.tool_stack.pop()

    def peek(self) -> int:
        """
        If tool_stack has values, the last one is the one on top.
        If not, then use self.front. self.front represent the first person in the queue, considering only the partial
        queue in my_stack
        Time, Space: O(1)
        """
        if self.tool_stack:
            return self.tool_stack[len(self.tool_stack) - 1]
        return self.front

    def empty(self) -> bool:
        return not self.my_stack and not self.tool_stack


if __name__ == "__main__":
    q = MyQueue()

    in_arr = [1,2]
    for i in in_arr:
        q.push(i)

    q.peek()

    print(q.pop())
    print(q.empty())

