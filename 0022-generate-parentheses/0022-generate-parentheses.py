class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ans = []
        def back(openPar,closePar):
            if openPar == closePar == n:
                ans.append("".join(stack))
                return
            if openPar < n:
                stack.append("(")
                back(openPar +1,closePar)
                stack.pop()
            if closePar < openPar:
                stack.append(")")
                back(openPar,closePar+1)
                stack.pop()
        back(0,0)
        return ans