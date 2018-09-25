class Solution:
    def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        
        To find the most frequently occuring element in an array
        """
        
            

        nums.sort()
        max_count = 1 
        target = nums[0]
        curr_count = 1
        n = len(nums)
        for i in range(1, n): 
            if (nums[i] == nums[i - 1]):
                curr_count += 1

            else :
                if (curr_count > max_count): 
                    max_count = curr_count
                    target = nums[i - 1]

                curr_count = 1

        
        if (curr_count > max_count):

            max_count = curr_count
            target = nums[n - 1]

        return target
    
    