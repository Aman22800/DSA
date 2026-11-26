class Solution:
    def canAliceWin(self, n: int) -> bool:
        c=10
        alice=True
        while n>=0:
            if alice:
                n-=c
                alice=False
                bob=True
                c-=1
            elif bob:
                n-=c
                bob=False
                alice=True
                c-=1
            print(n,alice,bob)
        return alice



            
