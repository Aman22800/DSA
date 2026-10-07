class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # Already all even or all odd
        if all(x % 2 == 0 for x in nums1):
            return True

        if all(x % 2 == 1 for x in nums1):
            return True

        # Mixed parity:
        # Need the smallest element to be odd
        return min(nums1) % 2 == 1