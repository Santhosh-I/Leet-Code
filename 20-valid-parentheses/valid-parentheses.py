class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        mapping = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

        for c in s:
            if c in mapping:
                stack.append(c)
            else:
                if not stack:
                    return False
                
                top = stack.pop()

                if mapping[top] != c:
                    return False

        return len(stack) == 0