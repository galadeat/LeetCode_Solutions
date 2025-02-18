class Solution:
    def factorial(n):
        if n in [0, 1]:
            return 1
        else:
            return n * factorial(n - 1)

    def count_primes(primes, n):
        count = 0
        for p in primes:
            if p <= n:
                count += 1
        return count

    def numPrimeArrangements(self, n: int) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                  43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        primes_num = Solution.count_primes(primes, n)
        res = Solution.factorial(primes_num) * Solution.factorial(n - primes_num)
        return res % 1000000007
