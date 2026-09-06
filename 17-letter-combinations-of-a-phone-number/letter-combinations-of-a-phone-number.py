class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        Dict={"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        if digits=="":
            return []
        self.combination=[]
        def comb(curr,i):
            if i>=len(digits):
                self.combination.append(curr)
                return
            for letter in Dict[digits[i]]:
                comb(curr+letter,i+1)
            return
        comb("",0)
        return self.combination
        

        