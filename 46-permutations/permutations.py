class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        # base case
        if len(nums) == 1:
            return [nums[:]]

        n = nums.pop(0)

        perms = self.permute(nums)

        result = []

        for perm in perms:
            for j in range(len(perm) + 1):
                result.append(perm[:j] + [n] + perm[j:])

        nums.insert(0, n)

        return result