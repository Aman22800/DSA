class Solution:
    def findMin(self, nums: list[int]) -> int:
        # BRUTE FROCE =>

        # n= len(nums)
        # minimum = nums[0]

        # for num in nums:
        #     if num < minimum:
        #         minimum = num
        # return minimum

        # OPTIMAL SOLUTION =>

        left = 0
        right = len(nums) -1

        while left < right:
            mid = left +(right-left)//2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
        