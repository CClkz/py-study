# 有效的括号

class Solution:
    # 栈结构的妙用
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        else:
            # 此处无法推测元素类型，故mypy会报错，加上list[str]
            arr: list[str] = []
            # 此处已经能推断出类型 dict[str, str]
            dict = {")": "(", "]": "[", "}": "{"}
            for char in s:
                leng = len(arr)
                if char == "(" or char == "[" or char == "{":
                    arr.append(char)
                elif leng == 0 or arr[leng-1] != dict[char]:
                    return False
                else:
                    arr.pop()
            return False if len(arr) else True

    # 栈，优化代码
    def isValid1(self, s):
        if len(s) % 2 == 1:
            return False

        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in pairs.values():
                stack.append(char)
            elif not stack or stack.pop() != pairs[char]:
                return False
        # not stack 判断空数组，等同于 len(stack) == 0，但效率更高
        return not stack
