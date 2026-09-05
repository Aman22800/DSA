
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:

        # Compute suffix minimum
        suffix_min = [0] * len(nums)
        curr_min = float('inf')

        for i in range(len(nums) - 1, -1, -1):
            curr_min = min(nums[i], curr_min)
            suffix_min[i] = curr_min

        # Compute prefix maximum and find first stable index
        currmax = float('-inf')

        for i in range(len(nums)):
            currmax = max(currmax, nums[i])

            score = currmax - suffix_min[i]

            if score <= k:
                return i

        return -1

