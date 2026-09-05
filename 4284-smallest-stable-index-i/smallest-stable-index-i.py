class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        #compute suffix min
        suffix_min=[0]*len(nums)
        curr_min=float('inf')
        for i in range(len(nums)-1,-1,-1):
            #print(i)
            curr_min=min(nums[i],curr_min)
            suffix_min[i]=curr_min
            print(suffix_min)


        currmax=float('-inf')

        for i in range(len(nums)):
            currmax=max(currmax,nums[i])

            score=currmax-suffix_min[i]
            if score<=k:
                return i
        return -1




            
            

        