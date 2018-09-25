
    def flipAndInvertImage(A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        Flipping an image
        """
        mylist = []
        B = []

        for item in A:
	        mylist.append(item[::-1])
	
        for li in mylist:
	        C=[]
	        C = [1 if x == 0 else 0 for x in li]
	        B.append(C)


        return(B)
