class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # def build(string):
        #     stack =[]
        #     for char in string:
        #         if char =="#":
        #             if stack:
        #                 stack.pop()
        #         else:
        #             stack.append(char)
        #     return ''.join(stack)
        # return build(s)==build(t)
        stack_t,stack_s = [] ,[]
        for chr in s:
            if chr == "#":
                if stack_s:
                    stack_s.pop()
            else:
                stack_s.append(chr)
        for chr in t:
            if chr == "#":
                if stack_t:
                    stack_t.pop()
            else:
                stack_t.append(chr)
        return stack_s == stack_t