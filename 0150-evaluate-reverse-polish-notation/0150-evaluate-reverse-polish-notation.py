class Solution:
    def operation(self,a,b,ch):
        a, b = int(a), int(b)
        if ch == "+":
            return a+b
        elif ch =="-":
            return a-b
        elif ch =="*":
            return a*b
        elif ch =="/":
            return a/b
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in range(len(tokens)):
            if tokens[i].lstrip('-').isdigit(): 
                stack.append(tokens[i])
            else:
                ch = tokens[i]
                b = stack.pop()
                a = stack.pop()
                stack.append(self.operation(a,b,ch))
        return int(stack[-1])