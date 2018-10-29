class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1 = [x for x in s]
        t1 = [x for x in t]
        
        s1.sort()
        t1.sort()
        #print(s1)
        #print(t1)
        if len(s1) == len(t1):
            for l in range(len(s1)):
                if s1[l] == t1[l]:
                    continue
                else:
                    return False
            return True
        else:
            return False