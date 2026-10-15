class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while n:
            #print(bin(n)[2:])
            count+=n&1
            #print(count)
            n>>=1
        return count

        