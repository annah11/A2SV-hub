class Solution:
    def scoreOfParentheses(self, s: str) -> int:
       
        stack = [0]  
        for i in s:
            if i == '(':
                stack.append(0)  
            else:
                rem = stack.pop()
                stack[-1] += max(2 * rem, 1)  
        return stack[0] 