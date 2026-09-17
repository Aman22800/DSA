class Solution:
    def trailingZeroes(self, n: int) -> int:
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        
        count=0
       
        while fact%10==0 and fact!=0:
            count+=1
            fact=fact//10
        return count

        