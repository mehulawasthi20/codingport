class Solution(object):
    def reverseWords(s):
        """
        :type s: str
        :rtype: str
        """
        

        str2 = s.split()
        mylst = []
        for strs in str2:
            mylst.append(strs[::-1])
            mylst.append(' ')
        if(len(mylst) != 0):
            mylst.pop()
        mystr = ''
        for strz in mylst:
            mystr += strz
        
            
        return mystr     

        
