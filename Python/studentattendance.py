class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        x = [i for i in s]
        if x.count('A') <= 1 and x.count('L') < 3:
            return True
            
            ''''
            for element in range(x):
                
                if x[element] == 'L' and x[element + 1] == 'L' and x[element + 2] =='L':
                    return False
                else:
                    continue
            '''
        elif x.count('A') <= 1 and x.count('L') >= 3:
            if 'LLL' in s:
                return False
            else:
                return True
        
        else:
            return False
            
            
            
                        
                