class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        nstr = []
        n1 = len(word1)
        n2 = len(word2)
        i,j = 0,0
        
        while i<n1 or j<n2:
            if(i<n1):
                nstr.append(word1[i])
            if(j<n2): 
                nstr.append(word2[j])
            i +=1
            j +=1
              

        return "".join(nstr)