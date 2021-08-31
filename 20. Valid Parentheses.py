class Solution:
    def isValid(self, s):
        temp=[None]
        tempdist={')':'(','}':'{',']':'['}
        for i in s:
            if i in tempdist and tempdist[i]==temp[len(temp)-1]:
                temp.pop()
            else:
                temp.append(i)
        return len(temp) == 1
        
