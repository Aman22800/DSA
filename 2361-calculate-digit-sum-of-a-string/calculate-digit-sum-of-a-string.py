class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            ans = []
            temp = []
            count = 0

            for i in range(len(s)):
                if count < k:
                    temp.append(int(s[i]))
                    count += 1
                else:
                    ans.append(sum(temp))
                    count = 1
                    temp = [int(s[i])]

            if temp:
                ans.append(sum(temp))

            s = ''.join(map(str, ans))

        return s