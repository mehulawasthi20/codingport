class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lst =[]
        if nums != None:
            
            for i in range(len(nums)):
                
                for j in range(i+1,len(nums)):
                    if nums[i] + nums[j] == target:
                        lst.append(i)
                        lst.append(j)
                        return(lst)
        
        else:
            return False

        
                