
    def sortArrayByParity(A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        B = [] 
        C = []
        D = []
        for element in A:
            if element % 2 == 0:
                B.append(element)
            else:
                C.append(element)
        D = B + C
        return D
        
