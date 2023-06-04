from StackArr import StackArr
from StackLinkedList import StackLinkedList
import math

class ReversePolishNotation:
    """"
    Input: tokens = ["2","1","+","3","*"]
    Output: 9
    Explanation: ((2 + 1) * 3) = 9

    Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    Output: 22
    Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
    = ((10 * (6 / (12 * -11))) + 17) + 5
    = ((10 * (6 / -132)) + 17) + 5
    = ((10 * 0) + 17) + 5
    = (0 + 17) + 5
    = 17 + 5
    = 22
    """
    def solution_arr_stack(self, arr):
        stack = StackArr()
        operation_list = ["+", "-", "*", "/"]

        for i in arr:
            if i not in operation_list:
                stack.push(int(i))
            else:
                right_item = stack.pop()
                left_item = stack.pop()
                print(f"Current operation: {left_item} {i} {right_item}")
                if i == "+":
                    stack.push(left_item + right_item)
                elif i == "-":
                    stack.push(left_item - right_item)
                elif i == "*":
                    stack.push(left_item * right_item)
                else:
                    stack.push(math.trunc(left_item / right_item))
        return stack.pop()

    def solution_ll_stack(self, arr):
        stack = StackLinkedList()
        operation_list = ["+", "-", "*", "/"]

        for i in arr:
            if i not in operation_list:
                stack.push(int(i))
            else:
                right_item = stack.pop()
                left_item = stack.pop()
                print(f"Current operation: {left_item} {i} {right_item}")
                if i == "+":
                    stack.push(left_item + right_item)
                elif i == "-":
                    stack.push(left_item - right_item)
                elif i == "*":
                    stack.push(left_item * right_item)
                else:
                    stack.push(math.trunc(left_item / right_item))
        return stack.pop()



if __name__ == "__main__":
    s = ReversePolishNotation()

    in_arr = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    res = s.solution_ll_stack(in_arr)
    print(res)