class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            "]": "[",
            ")": "(",
            "}": "{",
        }
        for char in s:
            if (char in "[{("):
                stack.append(char)
            else:
                if (len(stack) == 0):
                    return False
                if (stack[-1] != pairs[char]):
                    return False
                else:
                    stack.pop()

        if (len(stack) != 0):
            return False
        else:
            return True
