class Solution:
    def romanToInt(self, s):
        result = 0;
        Rnum = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}   
        for i in range(len(s)):                                      
            if(Rnum[s[i]]):                                          
                temp = Rnum[s[i]];
                if(i != 0 and Rnum[s[i-1]] < Rnum[s[i]]):              
                    temp = temp - (Rnum[s[i-1]])*2;                   
                result = result + temp ;
        return  result;
