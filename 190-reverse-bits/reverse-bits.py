class Solution:
    def reverseBits(self, n: int) -> int:
        result=0
        for _ in range(32):
            #take n=20
            # print("n",bin(n)[2:])
            # print("result",bin(result)[2:])
            bit=n&1
            result=(result<<1)|bit
            n>>=1
            
        return result
        