class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def generate(curr):
            if len(curr) == n:
                if curr not in nums:
                    return curr

                return ""

            add_zero = generate(curr + "0")
            if add_zero:
                return add_zero

            return generate(curr + "1")

        n = len(nums)
        nums = set(nums)
        return generate("")

# Source: https://leetcode.com/problems/find-unique-binary-string/solutions/4196840/find-unique-binary-string/?envType=daily-question&envId=2025-02-20