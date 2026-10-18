class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones = 0
        twos = 0

        for num in nums:
            # Ensure it is not in twos and add to ones bucket
            ones = (ones ^ num) & ~twos

            # Add to twos if already in ones bucket,
            # and remove from ones
            twos = (twos ^ num) & ~ones

            # If already in twos bucket, the third occurrence
            # removes the bit from both ones and twos

        return ones