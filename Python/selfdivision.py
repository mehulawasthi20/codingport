class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        
        def div(n):
            for x in str(n):
                if x == '0' or n % int(x) != 0:
                    return False
            return True
        sol = []
        for n in range(left,right + 1):
            if div(n):
                
                sol.append(n)
        return sol
        