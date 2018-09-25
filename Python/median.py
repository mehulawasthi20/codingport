#nums1 = [1,3]
#nums2 = [2]
def findMedianSortedArrays(nums1, nums2):
    '''
    Program to find the median of all numbers in two different arrays
    '''
        
    mylst1 = [x for x in nums1]
    
    for x in nums2:
        mylst1.append(x)
        
    mylst1.sort()
    
    length = len(mylst1) - 1
    l = len(mylst1)
    #print(len(mylst1))
    
    if(len(mylst1) % 2 == 0):
        median = (mylst1[int(length/2)] + mylst1[int((length/2) + 1)]) / 2
    else:
        median = mylst1[int(((l+1)/2) - 1)]
        pass
    
    print(median)
    