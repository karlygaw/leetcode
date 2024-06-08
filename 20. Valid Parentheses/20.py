class Solution:
    def isValid(self, s: str) -> bool:
        left = '({[' #открывающие скобки
        right = ')}]' #закрывающие скобки
        stack = []
        for char in s:
            if char in left: #если текущая открывающая
                stack.append(char)
            elif char in right:
                if len(stack) == 0:
                    return False
                if right.index(char) != left.index(stack.pop()):
                    return False

        return len(stack) == 0