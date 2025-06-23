class Solution:
    def calculateStack(self, s: str) -> int:
        stack = []
        cur_num = ""
        cur_operator = "+"

        for i in range(len(s)):
            char = s[i]
            # If current is integer
            if char.isdigit():
                cur_num += char
                if i+1 == len(s) or s[i+1] in ('+', '-', '*', '/') or s[i+1] == " ":
                    final_num = int(cur_num)
                    # print(final_num)
                    cur_num = ""
                    if cur_operator == '+':
                        stack.append(final_num)
                    elif cur_operator == '-':
                        stack.append(-final_num)
                    elif cur_operator == '*':
                        prev_num = stack.pop()
                        stack.append(prev_num * final_num)
                    else:
                        prev_num = stack.pop()
                        if (prev_num<0 and final_num>0) or (prev_num>0 and final_num<0):
                            stack.append(ceil(prev_num / final_num))
                        else:
                            stack.append(prev_num // final_num)
            elif char == " ":
                continue
            # If current is operator
            else:
                cur_operator = char
        # print(stack)
        return sum(stack)


    def calculateNoStack(self, s: str) -> int:
        cur_num = ""
        prev_num = None
        cur_operator = "+"
        res = 0

        for i in range(len(s)):
            char = s[i]
            # If current is integer
            if char.isdigit():
                cur_num += char
                if i + 1 == len(s) or s[i + 1] in ('+', '-', '*', '/') or s[i + 1] == " ":
                    final_num = int(cur_num)
                    cur_num = ""

                    if cur_operator == "+":
                        res = res + prev_num if prev_num else res
                        prev_num = final_num
                    elif cur_operator == "-":
                        res = res + prev_num if prev_num else res
                        prev_num = -final_num
                    elif cur_operator == '*':
                        prev_num = prev_num * final_num
                    else:
                        if (prev_num < 0 and final_num > 0) or (prev_num > 0 and final_num < 0):
                            prev_num = ceil(prev_num / final_num)
                        else:
                            prev_num = prev_num // final_num

            elif char == " ":
                continue
            # If current is operator
            else:
                cur_operator = char
        res = res + prev_num
        return res