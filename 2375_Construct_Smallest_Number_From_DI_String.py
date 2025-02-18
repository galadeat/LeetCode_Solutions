class Solution:

    def smallestNumber(self, pattern: str) -> str:

        def construct(index, value):

            if value == "D" and nums[index] < nums[index + 1]:
                nums[index], nums[index + 1] = nums[index + 1], nums[index]
            if value == "I" and nums[index] > nums[index + 1]:
                nums[index], nums[index + 1] = nums[index + 1], nums[index]

        nums = list(range(1, len(pattern) + 2))
        adjust = 10
        for _ in range(0, adjust):
            for index, value in enumerate(pattern):
                construct(index, pattern[index])
        return "".join(str(num) for num in nums)

