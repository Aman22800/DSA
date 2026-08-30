class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxcount=0
        seen=set(nums)
        for num in seen:
            if num-1 not in seen:
                count=1
                while num+count in seen:
                    count+=1
                maxcount=max(maxcount,count)
    
        return maxcount
        
        