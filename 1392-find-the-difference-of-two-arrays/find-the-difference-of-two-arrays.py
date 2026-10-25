class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        freq={}
        for i in nums1:
            if i not in freq:
                freq[i]=1
        freq2={}
        for j in nums2:
            if j not in freq2:
                freq2[j]=1

        ans1=[]

        
        for k in freq:
            if k not in freq2:
                ans1.append(k)
        ans2=[]
        for l in freq2:
            if l not in freq:
                ans2.append(l)
        result=[]
        result.append(ans1)
        result.append(ans2)
        return result
        