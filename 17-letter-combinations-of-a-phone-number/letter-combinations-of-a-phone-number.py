class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        Dict={"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}

        combo=[""]
        for d in digits:
            new_comb=[]

            for c in combo:
                for letter in Dict[d]:
                    new_comb.append(c+letter)
                    #print(new_comb)
            combo=new_comb
        return combo
        

        