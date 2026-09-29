class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        total = 0

        curr_max = 0
        max_sum = float('-inf')

        curr_min = 0
        min_sum = float('inf')

        for x in nums:
            total += x

            # Kadane's algorithm for maximum subarray
            curr_max = max(x, curr_max + x)
            max_sum = max(max_sum, curr_max)

            # Kadane's algorithm for minimum subarray
            curr_min = min(x, curr_min + x)
            min_sum = min(min_sum, curr_min)

        # If all numbers are negative,
        # total - min_sum would give 0 (empty subarray)
        if max_sum < 0:
            return max_sum

        # Maximum can either be:
        # 1. A normal subarray
        # 2. A circular subarray = total - minimum subarray
        return max(max_sum, total - min_sum)