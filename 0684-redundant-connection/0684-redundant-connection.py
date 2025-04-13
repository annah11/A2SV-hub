class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        m = len(edges)
        par = [i for i in range(m+1)]
        size = [1]*(m+1)
        def find(n):
            if n != par[n]:
                par[n]= find(par[n])
            return par[n]

        def unoin(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1 == p2:
                return False
            if size[p1] >size[p2]:
                par[p2] = p1
                size[p1] +=size[p2]
            else:
                par[p1] =p2
                size[p2] +=size[p1]


            return True
        for n1,n2 in edges:
            if not unoin(n1,n2):
                return [n1,n2]
