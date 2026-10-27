class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        key={}
        for i in arr:
            if i in key:
                key[i]+=1
            else:
                key[i]=1
        print(key)

        freq=set()
        for j in key:
            if key[j] in freq:
                return False
            else:
                freq.add(key[j])
        return True
        #print(freq)


        