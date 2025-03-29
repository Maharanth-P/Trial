class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        k=0
        for i in range(len(s)):
            l.append(s[i])
            if(s[i]==')'):
                if(l[k-1]!='('):
                    return False
                else:
                    l=l[:k-1]
                    k-=2
            if(s[i]==']'):
                if(l[k-1]!='['):
                    return False
                else:
                    l=l[:k-1]
                    k-=2
            if(s[i]=='}'):
                if(l[k-1]!='{'):
                    return False
                else:
                    l=l[:k-1]
                    k-=2
            k+=1
        if(len(l)>0):
            return False
        else:
            return True