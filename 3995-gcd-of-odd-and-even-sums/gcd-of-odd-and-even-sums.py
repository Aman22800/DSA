class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd=0
        even=0
        for i in range(1,2*n+1):
            if i%2==0:
                even+=i
            else:
                odd+=i
            #print(odd,"---",even)
        #return math.gcd(odd,even)

        while odd:
            even,odd=odd, even %odd
        return even
        

        