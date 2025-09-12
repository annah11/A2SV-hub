class Solution(object):
    def productQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        MOD = 10**9 + 7
        powers = []
        while n:
            x = n & -n
            powers.append(x)
            n -= x

        answers = []
        for l, r in queries:
            prod = 1
            for val in powers[l:r+1]:
                prod = (prod * val) % MOD
            answers.append(prod)

        return answers
