class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count=0
        for i in word:
            if ord(i)>64 and ord(i)<91:
                count+=1
        if count==len(word) or count==0:
            return True
        elif count==1 and word[0].isupper():
            return True
        else:
            return False        