class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False    

        strs=s
        d={}
        flag= True
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1

        for j in t:
            if j not in d:
                return False
            else:
                d[j]-=1
            
            if d[j]<0:
                return False
            
        return True
                
            

        
            

        