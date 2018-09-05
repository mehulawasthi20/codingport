class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
       #mylst = ["UD","DU","RL","LR"]
        r = 0
        l = 0
        u = 0
        d = 0
        for i in moves:
            if i == 'U':
                u = u + 1
            elif i == 'D':
                d = d + 1
            elif i == 'L':
                l = l + 1
            else:
                r = r + 1
        if( u == d and r == l):
        #result = (r - l) + (u - d)
            return True
        else:
            return False