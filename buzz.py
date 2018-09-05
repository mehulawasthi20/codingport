class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        mylst = []
        if n >= 1:
            for i in range(1,n+1):
                if(i % 3 == 0 and i % 5 == 0):
                    mylst.append("FizzBuzz")

                elif(i % 3 == 0):
                    mylst.append("Fizz")

                elif(i % 5 == 0):
                    mylst.append("Buzz")

                else:
                    mylst.append("{}".format(i))
        else:
            print("none")
        return(mylst)
            
        