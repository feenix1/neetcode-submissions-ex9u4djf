class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
                continue
            if char == ")":
                if len(stack) <= 0:
                    return False
                if stack.pop() != "(":
                    return False
                continue
            if char == "}":
                if len(stack) <= 0:
                    return False
                if stack.pop() != "{":
                    return False
                continue
            if char == "]":
                if len(stack) <= 0:
                    return False
                if stack.pop() != "[":
                    return False
                continue
        return len(stack) == 0