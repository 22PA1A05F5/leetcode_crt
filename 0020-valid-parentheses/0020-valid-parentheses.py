class Solution:
    def isValid(self, s: str) -> bool:
        string = {')': '(', '}':'{', ']': '['}
        stack = []
        for c in s:
            if c  not in string:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    p = stack.pop()
                    if p != string[c]:
                        return False
        return not stack