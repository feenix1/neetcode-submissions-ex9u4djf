class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            match char:
                case "+":
                    val2 = stack.pop(-1)
                    val1 = stack.pop(-1)
                    stack.append(val1 + val2)
                case "-":
                    val2 = stack.pop(-1)
                    val1 = stack.pop(-1)
                    stack.append(val1 - val2)
                case "*":
                    val2 = stack.pop(-1)
                    val1 = stack.pop(-1)
                    stack.append(val1 * val2)
                case "/":
                    val2 = stack.pop(-1)
                    val1 = stack.pop(-1)
                    stack.append(math.trunc(val1 / val2))
                case _:
                    stack.append(int(char))
        return stack[0]         