import math


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        if len(nums) > 1 and k > 0:
            nums[:] = nums[::-1]
            nums[:k] = nums[k - 1::-1]
            nums[k:] = nums[len(nums): k - 1: -1]

        """
        Do not return anything, modify nums in-place instead.
        """
