
    def numJewelsInStones(J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        tag = 0
        for i in J:
            for j in S:
                if i == j:
                    tag = tag + 1
        
        return tag
