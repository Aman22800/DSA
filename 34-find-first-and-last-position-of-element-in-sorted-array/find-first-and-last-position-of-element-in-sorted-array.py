class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left=0
        leftmost=-1
        right=len(nums)-1

        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                leftmost=mid
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        #print(leftmost)

        rightmost=-1
        left=0
        right=len(nums)-1

        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                rightmost=mid
                left=mid+1
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return [leftmost,rightmost]
            



        