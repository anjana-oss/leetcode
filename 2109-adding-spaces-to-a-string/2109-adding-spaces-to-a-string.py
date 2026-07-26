class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        word=[]
       
        j=0
        for i,c in enumerate(s):
            if j<len(spaces) and i==spaces[j]:
                word.append(" ")
                j+=1
            word.append(c)

        return "".join(word)
