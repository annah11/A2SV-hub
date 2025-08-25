class Solution(object):
    def distinctPrimeFactors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        primes = set()

        def primeFactors(num):
            d = 2
            while d * d <= num:
                while num % d == 0:
                    primes.add(d)
                    num //= d
                d += 1
            if num > 1:
                primes.add(num)

        for num in nums:
            primeFactors(num)

        return len(primes)
